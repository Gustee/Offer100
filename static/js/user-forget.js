//验证邮箱格式是否正确


    function mailformat(mailaddress) {
        var myReg = /^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/;
        if (myReg.test(mailaddress)) {
            return true;
        } else {
            return false;
        }
    }

//忘记密码
    $("#forget-password-button1").click(function () {
        var mailaddress = $("#mailaddress").val();
        console.log("1");

        if (mailformat(mailaddress) == false) {
            console.log("邮箱格式错误")
            $(".error-red-text").text("邮箱格式错误").show();
        } else {
            $.ajax({
                url: "/forget/",
                type: "POST",

                data: {
                    "mailaddress": mailaddress,
                    "csrfmiddlewaretoken": $('[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    console.log(data);
                    var returndata = JSON.parse(data);
                    console.log(returndata.msg);

                    if (returndata.msg == 1) {
                        console.log("邮箱未注册");
                        $(".error-red-text").text("邮箱未注册").show();
                    }
                }
            })
        }

    });

$("#forget-2").click(function(){
    console.log("加载注册脚本");
    jQuery.getScript("/static/js/user-signup.js")
});