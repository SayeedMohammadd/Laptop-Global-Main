var tpj = jQuery;

var revapi202;
tpj(document).ready(function() {
	if (tpj("#rev_slider_202_1").revolution == undefined) {
		revslider_showDoubleJqueryError("#rev_slider_202_1");
	} else {
		revapi202 = tpj("#rev_slider_202_1").show().revolution({
			sliderType : "standard",
			jsFileLocation : "assets/",
			sliderLayout : "auto",
			dottedOverlay : "none",
			delay : 5000,
			navigation : {
				keyboardNavigation : "on",
				keyboard_direction : "vertical",
				mouseScrollNavigation : "off",
				onHoverStop : "off",
				touch : {
					touchenabled : "off",
					swipe_threshold : 75,
					swipe_min_touches : 50,
					swipe_direction : "horizontal",
					drag_block_vertical : false
				},
				arrows : {
					style : "",
					enable : false,
					hide_onmobile : false,
					hide_onleave : false,
					hide_under : 0,
					hide_over : 9999,
					tmp : '',
					left : {
						h_align : "left",
						v_align : "center",
						h_offset : 50,
						v_offset : 0
					},
					right : {
						h_align : "right",
						v_align : "center",
						h_offset : 50,
						v_offset : 0
					}
				},
				bullets : {
					style : "",
					enable : false,
					hide_onmobile : false,
					hide_onleave : false,
					hide_delay : 200,
					hide_delay_mobile : 1200,
					hide_under : 0,
					hide_over : 9999,
					tmp : '<span class="tp-bullet-image"></span><span class="tp-bullet-title"></span>',
					direction : "horizontal",
					space : 0,
					h_align : "center",
					v_align : "bottom",
					h_offset : 0,
					v_offset : 0
				},
			},
			responsiveLevels : [1240, 1024, 778, 480],
			visibilityLevels : [1240, 1024, 778, 480],
			gridwidth : [1240, 1024, 778, 480],
			gridheight : [1050, 950, 960, 400],
			lazyType : "none",
			parallax : {
				type : "scroll",
				origo : "slidercenter",
				speed : 3000,
				levels : [5, 10, 15, 20, 25, 30, 35, 40, 45, 46, 47, 48, 49, 50, 100, 55],
				type : "scroll",
			},
			shadow : 0,
			spinner : "off",
			stopLoop : "on",
			stopAfterLoops : 0,
			stopAtSlide : 0,
			shuffle : "off",
			autoHeight : "off",
			fullScreenAutoWidth : "off",
			fullScreenAlignForce : "off",
			fullScreenOffsetContainer : "",
			fullScreenOffset : "60px",
			disableProgressBar : "on",
			hideThumbsOnMobile : "off",
			hideSliderAtLimit : 0,
			hideCaptionAtLimit : 0,
			hideAllCaptionAtLilmit : 0,
			debugMode : false,
			fallbacks : {
				simplifyAll : "off",
				nextSlideOnWindowFocus : "off",
				disableFocusListener : false,
			}
		});
	}
});
/*ready*/