$(document).ready(function(){
		$('.ui.dropdown').dropdown();		//下拉菜单

		$('.ui.radio.checkbox').checkbox();   //复选框
		display_now=document.getElementById("checkboxs technology");

		$('.special.cards .image').dimmer({     //鼠标移入出现按钮---info.html
          on: 'hover'
          });

		$(function () {                         //选择图片上传
            //按钮的点击事件
            $('#changeImage').click(function () {
                //触发file的点击事件
                $('#chooseImage').click();
            });
            //file的change事件
            $('#chooseImage').change(function () {
            	
            		    var filePath = $(this).val(),         //获取到input的value，里面是文件的路径  
	            fileFormat = filePath.substring(filePath.lastIndexOf(".")).toLowerCase(),  
	            src = window.URL.createObjectURL(this.files[0]); //转成可以在本地预览的格式  
	              
	        // 检查是否是图片  
	        if( !fileFormat.match(/.png|.jpg|.jpeg/) ) {  
	            error_prompt_alert('上传错误,文件格式必须为：png/jpg/jpeg');  
	            return;    
	        }  	    
	        $('#img').attr('src',src);  
            });
　　　　}); 
 

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

