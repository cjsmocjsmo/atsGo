function initLoadReviews() {
    $('.review1').empty();
    $.get('http://192.168.0.90:3200/AllApprovedReviews', function (data) {
        console.log(data);
        $.each(data, function (key, val) {
            let one = "<div class='rev-card'>";
            let two = "<div class='rev-card-body'>";
            let three = "<h5 class='rev-card-title'>Review</h5>";
            let four = "<p class='rev-cbod'>" + val.Message + "</p>";
            let five = "<p class='rev-csig'>" + val.Sig + "</p>";
            let six = "</div></div>";
            let newReview = one + two + three + four + five + six;
            $('.review1').append(newReview);
        })
    })
}

function initLoadQReviews() {
    $('.reviewadmin').empty();
    $.get('http://192.168.0.90:3200/AllQReviews', function (data) {
        console.log(data);
        $.each(data, function (key, val) {
            let one = "<div class='reviewTop' style='margin: 1em' id='" + val.UUID + "'>";
            let two = "<div class='qborder'>";
            let three = "<h5 >Review" + key + "</h5>";
            let threea = "<p>Name: " + val.Name + "</p>";
            let threeb = "<p>Email: " + val.Email + "</p>"
            let threec = "<p>Unique ID: " + val.UUID + "</p>"
            let four = "<p>Message: " + val.Message + "</p>";
            let five = "<p>Signature: " + val.Sig + "</p>";
            let six = "<button class='delBtn' data-delBtnId='" + val.UUID + "'>Delete Review</button></div></div>"
            let newReview = one + two + three + threea + threeb + threec + four + five + six;
            $('.reviewadmin').append(newReview);
        })
    })
}



$(document).on("click", "#revInput", function (event) {
    event.preventDefault();
    let name = $("#name").val();
    let email = $("#email").val();
    let message = $("#message").val();
    $.get('atq',
    {
        'name': name,
        'email': email,
        'message': message,
    },
    function (data) {
        console.log("sucess");
    })
    $("#name").val("");
    $("#email").val("");
    $("#message").val("");
    }
)
.on("click", ".delBtn", function() {
    let rtd = $(this).attr('data-delBtnId');
    let reviewToDeleteUUID = "#" + rtd
    $(reviewToDeleteUUID).empty();
    console.log(reviewToDeleteUUID)
    $.get('/DeleteReview',
    {
        'uuid': rtd,
    },
    function (data) {
        console.log("set Delete sucess");
    })
})
.on("click", "#accept", function(){
    $.get('/ProcessQuarintine',
    {},
    function (data) {
        console.log("set Delete sucess");
        // $('.reviewadmin').empty();
        let procMess = "<h1>All reviews processed</h1>"
        $('.reviewadmin').empty().append(procMess);
    })
})
.on("click", "#backup", function(){
    $.get('/Backup',
    {},
    function (data) {
        console.log("set Backup sucess");
    })
})
.on("click", "#name", function(){
    $("#name").val("")

})
.on("click", "#email", function(){
    $("#email").val("")
});


$(document).ready(function () {
    initLoadReviews();
    initLoadQReviews(); 
});