//注册按钮
    //应聘者
console.log("aaaa")
$("#signup-button-applicant").click(function () {
    console.log("aaaaa")
        var username = $("#can-username").val();
        var mailaddress = $("#can-mailaddress").val();
        var password = $("#can-password").val();
        var password2 = $("#can-password2").val;
        if (password == password2) {
            $(".error-red-text").text("两次密码输入不同").show();
            return;
        }
        if (username.length < 2 || password.length < 6) {
            console.log(username)
            console.log(password)
            console.log("账号或密码格式不对");
            $(".error-red-text").text("账号或密码格式不对").show();
        } else {
            $.ajax({
                url: "/signup/",
                type: "POST",

                data: {
                    "type": "applicant",
                    "username": username,
                    "password": password,
                    "mailaddress": mailaddress,
                    "csrfmiddlewaretoken": $('[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {

                    // console.log(data);
                    var returndata = JSON.parse(data);
                    console.log(returndata.msg);

                    if (returndata.msg == 1) {
                        console.log("邮箱已被使用");
                        $(".error-red-text").text("邮箱已被使用").show();
                    } else {
                        email = returndata.email
                        console.log(email)
                        window.location.replace("http://127.0.0.1:8000/talent_confirm_mail/?e="+email)
                    }
                }
            })
        }
    });
    //hr


$("#signup-1").click(function(){console.log(11)});

$("#signup-2").click(function(){
    console.log("加载注册脚本");
    jQuery.getScript("/static/js/user-signup.js")
});
$("#hr-button").click(function(){
    console.log("加载hr脚本");
    jQuery.getScript("/static/js/user-hr-signup.js")
})