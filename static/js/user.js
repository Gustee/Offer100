//login
//登录按钮
$(document).ready(function() {
    $('.ui.dropdown')
    .dropdown()
    ;
});


    $("#signin-button").click(function () {
        console.log('<<<<')
        var username = $("#username").val();
        var password = $("#password").val();
        if (username.length < 2 || password.length < 6) {
            console.log("账号或密码格式不对1");
            $(".error-red-text").text("账号或密码格式不对1").show();
        } else {
            $.ajax({
                url: "/login/",
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
                        console.log("账号或密码错误2");
                        $(".error-red-text").text("账号或密码错误2").show();
                    }
                    else{
                        window.location.replace("http://127.0.0.1:8000/job/")
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