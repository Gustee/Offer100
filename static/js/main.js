
    $(function () {
        $(".news .news-content a").mouseover(function () {
            $this = $(this);
            $this.find(".pic1").hide();
            $this.find(".pic2").show();
            $this.children().css("color", "#12c3f9")
            $this.find(".qrcode").show();
        })
        $(".news .news-content a").mouseout(function () {
            $this = $(this);
            $this.find(".pic1").show();
            $this.find(".pic2").hide();
            $this.children().css("color", "#9c9c9c");
            $this.find(".qrcode").hide();
        })
        $(".imgN").mouseover(function () {
            $this = $(this);
            $this.children().eq(0).hide();
            $this.children().eq(1).show();
        })
        $(".imgN").mouseout(function () {
            $this = $(this);
            $this.children().eq(0).show();
            $this.children().eq(1).hide();
        })
        //轮播
        function lunb() {
            var n = $(".lunbo ul li").index($(".lunbo ul li.show"));
            if (n != 2) {
                $(".lunbo ul li").eq(n).removeClass("show").next().addClass("show")
            } else {
                $(".lunbo ul li").eq(2).removeClass("show");
                $(".lunbo ul li").eq(0).addClass("show");
            }

        }
        var time = setInterval(lunb, 2000);
        //触摸清楚定时器
        $(".lunbo").mouseover(function () {
            clearInterval(time)
        })
        $(".lunbo").mouseout(function () {
            time = setInterval(lunb, 2000);
        })
        //按钮
        $(".left-btn").click(function () {
            var n = $(".lunbo ul li").index($(".lunbo ul li.show"));
            if (n != 0) {
                $(".lunbo ul li").eq(n).removeClass("show").prev().addClass("show")
            } else {
                $(".lunbo ul li").eq(0).removeClass("show");
                $(".lunbo ul li").eq(2).addClass("show");
            }
        })
        $(".right-btn").click(function () {
            var n = $(".lunbo ul li").index($(".lunbo ul li.show"));
            if (n != 2) {
                $(".lunbo ul li").eq(n).removeClass("show").next().addClass("show")
            } else {
                $(".lunbo ul li").eq(2).removeClass("show");
                $(".lunbo ul li").eq(0).addClass("show");
            }
        })
        //footer 图片
        $("#weixinqr").mouseover(function(){
            $('.weixin-grey').css("display","none");
            $('.weixin').css("display","inline-block");
            $('.qrcode').css("display","block")
        })
        $("#weixinqr").mouseout(function(){
            $('.weixin-grey').css("display","inline-block");
            $('.weixin').css("display","none");
            $('.qrcode').css("display","none");
        })
        $("#weibo").mouseover(function(){
            $('.weibo-grey').css("display","none");
            $('.weibo').css("display","inline-block");
        })
        $("#weibo").mouseout(function(){
            $('.weibo-grey').css("display","inline-block");
            $('.weibo').css("display","none");
        })
        $("#blog").mouseover(function(){
            $('.blog-grey').css("display","none");
            $('.blog').css("display","inline-block");
        })
        $("#blog").mouseout(function(){
            $('.blog-grey').css("display","inline-block");
            $('.blog').css("display","none");
        })
        $("#blog").mouseover(function(){
            $('.blog-grey').css("display","none");
            $('.blog').css("display","inline-block");
        })
        $("#blog").mouseout(function(){
            $('.blog-grey').css("display","inline-block");
            $('.blog').css("display","none");
        })
        $("#linkedin").mouseover(function(){
            $('.linkedin-grey').css("display","none");
            $('.linkedin').css("display","inline-block");
        })
        $("#linkedin").mouseout(function(){
            $('.linkedin-grey').css("display","inline-block");
            $('.linkedin').css("display","none");
        })
    })
