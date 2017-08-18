console.log('123');

$(function () {
    console.log('begin');
    var x = 10;
    var y = 20;
    console.log('begin2');

    $("#wang").mouseover(function (e) {
        console.log('1');
        var code = "<div id='code' style='position:absolute;border:1px solid #999; background:#ffffff;padding:0px;'><img src=\"https://open.weixin.qq.com/qr/code/?username=gh_4da7eb434f20\" alt='qrcode' width='150'></div>";
        $("body").append(code);
        $("#code").css({
            "top": (e.pageY - y) + "px",
            "left": (e.pageX + x) + "px"
        }).show("fast");
    }).mouseout(function () {
        $("#code").remove();
    });
    console.log('begin3');

    // $("#code").touchstart(function () {
    //     console.log('remove');
    //     $("#code").remove();
    // });
    console.log('?');
    $("#chengyu").mouseover(function (e) {
        console.log("?");
        var du_code = "<div id='du_code' style='position:absolute;border:1px solid #999; background:#ffffff;padding:0px;'><img src=\"https://open.weixin.qq.com/qr/code/?username=gh_f674606e4e46\" alt='qrcode' width='150'></div>";
        $("body").append(du_code);
        $("#du_code").css({
            "top": (e.pageY - y) + "px",
            "left": (e.pageX + x) + "px"
        }).show("fast");
    }).mouseout(function () {
        $("#du_code").remove();
    });
    $("#du_code").touchstart(function () {
        $("#du_code").remove();
    });
});
