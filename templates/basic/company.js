/*
 * Created by xjx on 2016/7/14.
 */
$(function () {
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

})
