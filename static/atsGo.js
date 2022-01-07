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
            console.log(newReview);
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
            console.log(newReview);
            $('.reviewadmin').append(newReview);
        })
    })
}

$(document).ready(function () {
    initLoadReviews();
    initLoadQReviews();
    $("#revInput").click(function (event) {
    event.preventDefault();
    let name = $("#name").val();
    let email = $("#email").val();
    let message = $("#message").val();
    console.log(name);
    console.log(email);
    console.log(message);
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
    });

    $(".delBtn").click(function(){
        let reviewToDeleteUUID = $(this).attr('data-delBtnId');
        $("#reviewToDeleteUUID").empty();
        $.get('DeleteReview',
        {
            'uuid': reviewToDeleteUUID,
        },
        function (data) {
            console.log("set Delete sucess");
        })

    })
});