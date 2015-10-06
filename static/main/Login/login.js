jQuery(function($){
    $.supersized({
        // Functionality
        slide_interval     : 4000,    // Length between transitions
        transition         : 1,    // 0-None, 1-Fade, 2-Slide Top, 3-Slide Right, 4-Slide Bottom, 5-Slide Left, 6-Carousel Right, 7-Carousel Left
        transition_speed   : 1000,    // Speed of transition
        performance        : 1,    // 0-Normal, 1-Hybrid speed/quality, 2-Optimizes image quality, 3-Optimizes transition speed // (Only works for Firefox/IE, not Webkit)

        // Size & Position
        min_width          : 0,    // Min width allowed (in pixels)
        min_height         : 0,    // Min height allowed (in pixels)
        vertical_center    : 1,    // Vertically center background
        horizontal_center  : 1,    // Horizontally center background
        fit_always         : 0,    // Image will never exceed browser width or height (Ignores min. dimensions)
        fit_portrait       : 1,    // Portrait images will not exceed browser height
        fit_landscape      : 0,    // Landscape images will not exceed browser width

        // Components
        slide_links        : 'blank',    // Individual links for each slide (Options: false, 'num', 'name', 'blank')
        slides             : [    // Slideshow Images
                                 {image : '/static/main/Login/backgrounds/4.jpg'},
                                 {image : '/static/main/Login/backgrounds/2.jpg'},
                                 {image : '/static/main/Login/backgrounds/3.jpg'}
                       ]
    });
});


function submit_info() {
	$.ajax({
		beforeSend: function(){
			if($("#username").val().length == 0){
				show_info("请填写用户名");
				$('#username').focus();
				return false;
			}
		},
		type:'POST',
		url:'/login.ajax',
		data: {
			"username": $("#username").val(),
			"password": $("#password").val(),
			"next": $("#submit_bt").attr("data-next"),
		},
		dataType : "json",
        success: function(data) {
        	if(data["status"] == 0){
        		location.href = data["next_url"];
        	}else{
        		show_info(data["message"]);
        	}
    	},
		error: function(e) {
			show_info("登录失败");
		}
	});
}

function show_info(info){
	$(".error").html(info).show();
}

$(function(){
    $(".username").keydown(function(){
        $(".password").val("");
        $(".error").hide();
    })
});