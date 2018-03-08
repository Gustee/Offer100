$(document).ready(function(){
		$('.ui.dropdown').dropdown();
		$('.ui.radio.checkbox').checkbox();
		display_now=document.getElementById("checkboxs technology");
})
var display_now;
function f1(){
	var x=document.getElementById("path").value;
	var y1=document.getElementById("checkboxs technology");
	var y2=document.getElementById("checkboxs data");
	var y3=document.getElementById("checkboxs product");
	var y4=document.getElementById("checkboxs design");
	var y5=document.getElementById("checkboxs marketsell");
	var y6=document.getElementById("checkboxs function");
	var y7=document.getElementById("checkboxs run");
	if(x==1){
		display_now.style.position="absolute";
		display_now.style.display="none";
		y1.style.position="static";
		y1.style.display="inline";
		display_now=y1;
	}
	if(x==2){
		display_now.style.position="absolute";
		display_now.style.display="none";
		y2.style.position="static";
		y2.style.display="inline";
		display_now=y2;
	}
	if(x==3){
		display_now.style.position="absolute";
		display_now.style.display="none";
		y3.style.position="static";
		y3.style.display="inline";
		display_now=y3;
	}
	if(x==4){
		display_now.style.position="absolute";
		display_now.style.display="none";
		y4.style.position="static";
		y4.style.display="inline";
		display_now=y4;
	}
	if(x==5){
		display_now.style.position="absolute";
		display_now.style.display="none";
		y5.style.position="static";
		y5.style.display="inline";
		display_now=y5;
	}
	if(x==6){
		display_now.style.position="absolute";
		display_now.style.display="none";
		y6.style.position="static";
		y6.style.display="inline";
		display_now=y6;
	}
	if(x==7){
		display_now.style.position="absolute";
		display_now.style.display="none";
		y7.style.position="static";
		y7.style.display="inline";
		display_now=y7;
	}

}
$('#save-1').click(function(){
	console.log($('#username').val().toString().length)
	if($('#username').val().toString().length<1||$('#sex').val().toString().length<1||$('#age').val().toString().length<1||$('#country').val().toString().length<1||$('#phoneNum').val().toString().length<1||$('#email').val().toString().length<1){
		console.log("请输入完整信息");
        $(".error-red-text").text("请输入完整信息").show();
	}
	// $.ajax({
	// 	url: "/info/",
	// 	type: "POST",
	// 	data:{
	// 		"username":$('#username').val(),
	// 		"sex":$('#sex').val(),
	// 		"age":$('#age').val(),
	// 		"country":$('#country').val(),
	// 		"phone":$('#phoneNum').val(),
	// 		"email":$('#email').val(),
	// 		"csrfmiddlewaretoken": $('[name=csrfmiddlewaretoken]').val()
     //    },
     //    success:{
    //
	// 	}
     //    })
	// })
});

