//login
//登录按钮
    $("#signin-button").click(function () {
        var username = $("#username").val();
        var password = $("#password").val();
        if (username.length < 5 || password.length < 6) {
            console.log("账号或密码格式不对");
            $(".error-red-text").text("账号或密码格式不对").show();
        } else {
            $.ajax({
                url: "/signin/",
                type: "POST",

                data: {
                    "username": $("#username").val(),
                    "password": $("#password").val(),
                    "csrfmiddlewaretoken": $('[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    console.log(data);
                    var returndata = JSON.parse(data);
                    console.log(returndata.msg);

                    if (returndata.msg == 1) {
                        console.log("账号或密码错误");
                        $(".error-red-text").text("账号或密码错误").show();
                    }
                }
            })
        }
    });


//test
$("#signin-1").click(function(){
    console.log("加载注册脚本");
    jQuery.getScript("/static/js/user-signup.js")
});
$("#signin-2").click(function(){
    console.log("加载忘记密码脚本");
    jQuery.getScript("/static/js/user-forget.js")
});