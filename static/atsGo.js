// kitsap
// 20200520_143645_thumb.webp  20200703_122229_thumb.webp  20201112_105838_thumb.webp  20201121_142519_thumb.webp
// 20200703_122208_thumb.webp  20201112_101000_thumb.webp  20201112_112326_thumb.webp  20201121_154742_thumb.webp
// 20200703_122216_thumb.webp  20201112_103812_thumb.webp  20201112_120634_thumb.webp  20210114_111858_thumb.webp
// 20200703_122218_thumb.webp  20201112_104612_thumb.webp  20201119_100147_thumb.webp  20210114_111902_thumb.webp
// 20200703_122219_thumb.webp  20201112_104620_thumb.webp  20201121_141544_thumb.webp  20210114_113656_thumb.webp
// 20200703_122220_thumb.webp  20201112_105832_thumb.webp  20201121_141549_thumb.webp  20210114_113707_thumb.webp

// 20200520_143645_orig.webp  20200703_122229_orig.webp  20201112_105838_orig.webp  20201121_142519_orig.webp
// 20200703_122208_orig.webp  20201112_101000_orig.webp  20201112_112326_orig.webp  20201121_154742_orig.webp
// 20200703_122216_orig.webp  20201112_103812_orig.webp  20201112_120634_orig.webp  20210114_111858_orig.webp
// 20200703_122218_orig.webp  20201112_104612_orig.webp  20201119_100147_orig.webp  20210114_111902_orig.webp
// 20200703_122219_orig.webp  20201112_104620_orig.webp  20201121_141544_orig.webp  20210114_113656_orig.webp
// 20200703_122220_orig.webp  20201112_105832_orig.webp  20201121_141549_orig.webp  20210114_113707_orig.webp

// mason 
// 20201121_141608_orig.webp  20210114_130013_orig.webp  20210114_144538_orig.webp  20210709_093724_orig.webp
// 20201121_141826_orig.webp  20210114_131757_orig.webp  20210703_114202_orig.webp  20210709_093733_orig.webp
// 20201121_141838_orig.webp  20210114_131804_orig.webp  20210703_114203_orig.webp  20210728_110226_orig.webp
// 20201121_141845_orig.webp  20210114_131809_orig.webp  20210703_114205_orig.webp  20210728_110233_orig.webp
// 20201121_154747_orig.webp  20210114_140603_orig.webp  20210709_093636_orig.webp  20210728_110344_orig.webp
// 20201121_154954_orig.webp  20210114_141802_orig.webp  20210709_093705_orig.webp  20210901_110234_orig.webp

// 20201121_141608_thumb.webp  20210114_130013_thumb.webp  20210114_144538_thumb.webp  20210709_093724_thumb.webp
// 20201121_141826_thumb.webp  20210114_131757_thumb.webp  20210703_114202_thumb.webp  20210709_093733_thumb.webp
// 20201121_141838_thumb.webp  20210114_131804_thumb.webp  20210703_114203_thumb.webp  20210728_110226_thumb.webp
// 20201121_141845_thumb.webp  20210114_131809_thumb.webp  20210703_114205_thumb.webp  20210728_110233_thumb.webp
// 20201121_154747_thumb.webp  20210114_140603_thumb.webp  20210709_093636_thumb.webp  20210728_110344_thumb.webp
// 20201121_154954_thumb.webp  20210114_141802_thumb.webp  20210709_093705_thumb.webp

// pierce 
// 20210114_140555_orig.webp  20210901_110605_orig.webp  20210907_161104_orig.webp  20211022_082327_orig.webp
// 20210114_141712_orig.webp  20210901_110619_orig.webp  20210907_174135_orig.webp  20211022_083103_orig.webp
// 20210901_110237_orig.webp  20210901_110629_orig.webp  20210918_105104_orig.webp  20211023_111603_orig.webp
// 20210901_110253_orig.webp  20210907_161051_orig.webp  20210918_105122_orig.webp  20211023_111607_orig.webp
// 20210901_110316_orig.webp  20210907_161053_orig.webp  20210918_105132_orig.webp  20211023_111619_orig.webp
// 20210901_110336_orig.webp  20210907_161055_orig.webp  20210918_112452_orig.webp  received_2816359661929547_orig.webp
// 20210901_110340_orig.webp  20210907_161102_orig.webp  20211021_145212_orig.webp  received_3341614045887235_orig.webp

// 20210114_140555_thumb.webp  20210901_110605_thumb.webp  20210907_174135_thumb.webp  20211023_111603_thumb.webp
// 20210114_141712_thumb.webp  20210901_110619_thumb.webp  20210918_105104_thumb.webp  20211023_111607_thumb.webp
// 20210901_110234_thumb.webp  20210901_110629_thumb.webp  20210918_105122_thumb.webp  20211023_111619_thumb.webp
// 20210901_110237_thumb.webp  20210907_161051_thumb.webp  20210918_105132_thumb.webp  received_2816359661929547_thumb.webp
// 20210901_110253_thumb.webp  20210907_161053_thumb.webp  20210918_112452_thumb.webp  received_3341614045887235_thumb.webp
// 20210901_110316_thumb.webp  20210907_161055_thumb.webp  20211021_145212_thumb.webp
// 20210901_110336_thumb.webp  20210907_161102_thumb.webp  20211022_082327_thumb.webp
// 20210901_110340_thumb.webp  20210907_161104_thumb.webp  20211022_083103_thumb.webp



function initLoadReviews() {
    $('.review1').empty();
    $.get('/AllApprovedReviews', function (data) {
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
    $.get('/AllQReviews', function (data) {
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

function fadeinout() {
    $('.aniMain').delay(2750).fadeOut(750);
    $('.mainDiv').delay(3575).fadeIn(1000);
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
})
    .on("click", ".delBtn", function () {
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
    .on("click", "#accept", function () {
        $.get('/ProcessQuarintine',
            {},
            function (data) {
                console.log("set Delete sucess");
                // $('.reviewadmin').empty();
                let procMess = "<h1>All reviews processed</h1>"
                $('.reviewadmin').empty().append(procMess);
            })
    })
    .on("click", "#backup", function () {
        $.get('/Backup',
            {},
            function (data) {
                console.log("set Backup sucess");
            })
    })
    .on("click", "#name", function () {
        $("#name").val("")

    })
    .on("click", "#email", function () {
        $("#email").val("")
    });


$(document).ready(function () {
    fadeinout();
    initLoadReviews();
    initLoadQReviews();
    
});