package main

import (
	"context"
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"github.com/gorilla/mux"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"gopkg.in/yaml.v2"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
	// "os"
	"os/exec"
	"strings"
	"time"
)

///////////////////////////////////////////////////////////////////////////////

func UUID() (string, error) {
	uuid := make([]byte, 16)
	n, err := rand.Read(uuid)
	if n != len(uuid) || err != nil {
		return "", err
	}
	uuid[8] = 0x80
	uuid[4] = 0x40
	boo := hex.EncodeToString(uuid)
	return boo, nil
}

///////////////////////////////////////////////////////////////////////////////

func Close(client *mongo.Client, ctx context.Context, cancel context.CancelFunc) {
	defer cancel()
	defer func() {
		if err := client.Disconnect(ctx); err != nil {
			panic(err)
		}
	}()
}

func Connect(uri string) (*mongo.Client, context.Context, context.CancelFunc, error) {
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	client, err := mongo.Connect(ctx, options.Client().ApplyURI(uri))
	return client, ctx, cancel, err
}

func InsertOne(client *mongo.Client, ctx context.Context, dataBase, col string, doc interface{}) (*mongo.InsertOneResult, error) {
	collection := client.Database(dataBase).Collection(col)
	result, err := collection.InsertOne(ctx, doc)
	return result, err
}

func UpdateOne(client *mongo.Client, ctx context.Context, filter interface{}, dataBase string, col string, update interface{}) (*mongo.UpdateResult, error) {
	collection := client.Database(dataBase).Collection(col)
	result, err := collection.UpdateOne(ctx, filter, update, options.Update().SetUpsert(true))
	return result, err
}

func Query(client *mongo.Client, ctx context.Context, dataBase, col string, query, field interface{}) (result *mongo.Cursor, err error) {
	collection := client.Database(dataBase).Collection(col)
	result, err = collection.Find(ctx, query, options.Find().SetProjection(field))
	return
}

func CheckError(err error, msg string) {
	if err != nil {
		fmt.Println(msg)
		log.Println(msg)
		log.Println(err)
		panic(err)
	}
}

///////////////////////////////////////////////////////////////////////////////

func ShowMain(w http.ResponseWriter, r *http.Request) {
	tmppath := "./static/alphatree.html"
	tmpl := template.Must(template.ParseFiles(tmppath))
	tmpl.Execute(w, tmpl)
}

func ShowAdmin(w http.ResponseWriter, r *http.Request) {
	showtmppath := "./static/admin.html"
	showtmpl := template.Must(template.ParseFiles(showtmppath))
	showtmpl.Execute(w, showtmpl)
}

func AlphaT_Insert(db string, coll string, ablob ReviewStruct) {
	client, ctx, cancel, err := Connect("mongodb://db:27017/ampgodb")
	CheckError(err, "AlphaT_Insert_: Connections has failed")
	defer Close(client, ctx, cancel)
	_, err2 := InsertOne(client, ctx, db, coll, ablob)
	CheckError(err2, "AlphaT_Insert_has failed")
}

func AddToQuarantineHandler(w http.ResponseWriter, r *http.Request) {
	uuid, _ := UUID()
	var name string = r.URL.Query().Get("name")
	var email string = r.URL.Query().Get("email")
	var message string = r.URL.Query().Get("message")
	var sig string
	if name != "" {
		sig = name
	} else if email != "" {
		s := strings.Split(email, "@")
		sig = s[0]
	} else {
		sig = ""
	}

	ct := time.Now()
	date := ct.Format("01-01-2021")

	var newReview = ReviewStruct{
		UUID:       uuid,
		Date:       date,
		Name:       name,
		Email:      email,
		Sig:        sig,
		Message:    message,
		Approved:   "no",
		Quarintine: "yes",
		Delete:     "no",
	}
	AlphaT_Insert("maindb", "main", newReview)
}

func AllQuarintineReviewsHandler(w http.ResponseWriter, r *http.Request) {
	filter := bson.M{"approved": "no", "quarintine": "yes", "delete": "no"}
	opts := options.Find()
	opts.SetProjection(bson.M{"_id": 0})
	client, ctx, cancel, err := Connect("mongodb://db:27017/alphatree")
	defer Close(client, ctx, cancel)
	CheckError(err, "MongoDB connection has failed")
	coll := client.Database("maindb").Collection("main")
	cur, err := coll.Find(context.TODO(), filter, opts)
	CheckError(err, "AllQuarintineReviews find has failed")
	var allQRevs []ReviewStruct
	if err = cur.All(context.TODO(), &allQRevs); err != nil {
		log.Fatal(err)
	}
	log.Printf("%s this is AllQuarintineReviews-", allQRevs)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(&allQRevs)
	log.Println("AllQuarintineReviews Info Complete")
}

func AllApprovedReviewsHandler(w http.ResponseWriter, r *http.Request) {
	filter := bson.M{"approved": "yes", "quarintine": "no", "delete": "no"}
	opts := options.Find()
	opts.SetProjection(bson.M{"_id": 0})
	client, ctx, cancel, err := Connect("mongodb://db:27017/alphatree")
	defer Close(client, ctx, cancel)
	CheckError(err, "MongoDB connection has failed")
	coll := client.Database("maindb").Collection("main")
	cur, err := coll.Find(context.TODO(), filter, opts)
	CheckError(err, "AllReviews find has failed")
	var allRevs []ReviewStruct
	if err = cur.All(context.TODO(), &allRevs); err != nil {
		log.Fatal(err)
	}
	log.Printf("%s this is AllReviews-", allRevs)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(&allRevs)
	log.Println("AllReviews Info Complete")
}

func SetReviewToDeleteHandler(w http.ResponseWriter, r *http.Request) {
	var delUUID string = r.URL.Query().Get("uuid")
	filter := bson.M{"uuid": delUUID}
	update := bson.M{"$set": bson.M{"delete": "yes"}}
	client, ctx, cancel, err := Connect("mongodb://db:27017/alphatree")
	defer Close(client, ctx, cancel)
	CheckError(err, "MongoDB connection has failed")
	UpdateOne(client, ctx, filter, "maindb", "main", update)
}

func ProcessQuarantineHandler(w http.ResponseWriter, r *http.Request) {
	filter := bson.M{}
	opts := options.Find()
	opts.SetProjection(bson.M{"_id": 0})
	client, ctx, cancel, err := Connect("mongodb://db:27017/alphatree")
	defer Close(client, ctx, cancel)
	CheckError(err, "MongoDB connection has failed")
	coll := client.Database("maindb").Collection("main")
	cur, err := coll.Find(context.TODO(), filter, opts)
	CheckError(err, "AllQuarintineReviews find has failed")
	var allRevs []ReviewStruct
	if err = cur.All(context.TODO(), &allRevs); err != nil {
		log.Fatal(err)
	}
	log.Printf("%s this is AllQuarintineReviews-", allRevs)

	for _, rev := range allRevs {
		filter := bson.M{"uuid": rev.UUID}
		update := bson.M{"$set": bson.M{"approved": "yes", "quarintine": "no"}}
		client, ctx, cancel, err := Connect("mongodb://db:27017/alphatree")
		defer Close(client, ctx, cancel)
		CheckError(err, "MongoDB connection has failed")
		UpdateOne(client, ctx, filter, "maindb", "main", update)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode("Update complete")
	log.Println("AllQuarintineReviews Info Complete")
}

func BackupReviewHandler(w http.ResponseWriter, r *http.Request) {
	exec.Command("/bin/sh", "./backup/backup.sh")
	content, err := ioutil.ReadFile("/backup/backup.json") // the file is inside the local directory
	if err != nil {
		fmt.Println("Err")
	}
	fmt.Println(content)

}

// INIT STUFF
type ReviewStruct struct {
	UUID       string `yaml:"UUID"`
	Date       string `yaml:"Date"`
	Name       string `yaml:"Name"`
	Email      string `yaml:"Email"`
	Sig        string `yaml:"Sig"`
	Message    string `yaml:"Message"`
	Approved   string `yaml:"Approved"`
	Quarintine string `yaml:"Quarintine"`
	Delete     string `yaml:"Delete"`
}

func (c *ReviewStruct) Parse(data []byte) error {
	return yaml.Unmarshal(data, c)
}

func init() {
	data, err := ioutil.ReadFile("./static/review1.yaml")
	if err != nil {
		log.Fatal(err)
	}

	var rev1 ReviewStruct
	if err := rev1.Parse(data); err != nil {
		log.Fatal(err)
	}
	fmt.Println(rev1)
	AlphaT_Insert("maindb", "main", rev1)

	data2, err := ioutil.ReadFile("./static/review2.yaml")
	if err != nil {
		log.Fatal(err)
	}

	var rev2 ReviewStruct
	if err := rev2.Parse(data2); err != nil {
		log.Fatal(err)
	}
	fmt.Println(rev2)
	AlphaT_Insert("maindb", "main", rev2)

	data3, err := ioutil.ReadFile("./static/fake1.yaml")
	if err != nil {
		log.Fatal(err)
	}

	var rev3 ReviewStruct
	if err := rev3.Parse(data3); err != nil {
		log.Fatal(err)
	}
	fmt.Println(rev3)
	AlphaT_Insert("maindb", "main", rev3)

	data4, err := ioutil.ReadFile("./static/fake2.yaml")
	if err != nil {
		log.Fatal(err)
	}

	var rev4 ReviewStruct
	if err := rev4.Parse(data4); err != nil {
		log.Fatal(err)
	}
	fmt.Println(rev4)
	AlphaT_Insert("maindb", "main", rev4)

}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/alphatree", ShowMain)
	r.HandleFunc("/admin", ShowAdmin)
	r.HandleFunc("/AllQReviews", AllQuarintineReviewsHandler)
	r.HandleFunc("/AllApprovedReviews", AllApprovedReviewsHandler)
	r.HandleFunc("/ProcessQuarintine", ProcessQuarantineHandler)
	r.HandleFunc("/Backup", BackupReviewHandler)
	r.HandleFunc("/DeleteReview", SetReviewToDeleteHandler)
	r.HandleFunc("/atq", AddToQuarantineHandler)
	r.PathPrefix("/static/").Handler(http.StripPrefix("/static/", http.FileServer(http.Dir("./static/"))))
	port := ":3200"
	http.ListenAndServe(port, (r))
}
