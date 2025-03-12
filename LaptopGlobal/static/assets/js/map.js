$(function() {"use strict";

	var video1;
	var left_off;
	var top_off;

	//Custom Map
	if ($('#map-view').length) {

		//41.828597, -73.762763
		var pos = new google.maps.LatLng(41.236859, -73.667425);

		var map = new google.maps.Map(document.getElementById('map-view'), {
			zoom : 16,
			center : pos,
			scrollwheel : false,
			//mapTypeId : google.maps.MapTypeId.ROADMAP,
			streetViewControl : false,
			zoomControl : false,
			//mapTypeControl : false
		});
		//map.mapTypes.set('map_style', styledMap);
		//map.setMapTypeId('map_style');
		var pos1 = new google.maps.LatLng(41.235882, -73.669761);
		var pos2 = new google.maps.LatLng(41.234500, -73.668920);
		var pos3 = new google.maps.LatLng(41.232900, -73.675630);
		var pos4 = new google.maps.LatLng(41.235700, -73.661240);
		var pos5 = new google.maps.LatLng(41.237600, -73.668350);
		var pos6 = new google.maps.LatLng(41.234300, -73.675960);

		var marker1 = new google.maps.Marker({
			position : pos1,
			map : map,
			draggable : false,
			icon : 'assets/images/map-icon-2.png',

		});

		var marker2 = new google.maps.Marker({
			position : pos2,
			map : map,
			draggable : false,
			icon : 'assets/images/map-icon-2.png'

		});
		var marker3 = new google.maps.Marker({
			position : pos3,
			map : map,
			draggable : false,
			icon : 'assets/images/map-icon-2.png'

		});
		var marker4 = new google.maps.Marker({
			position : pos4,
			map : map,
			draggable : false,
			icon : 'assets/images/map-icon-2.png',

		});

		var con = $('#location1').html();
		var infowindow_1 = new google.maps.InfoWindow({
			content : con,
			maxWidth : 200,
			pixelOffset : new google.maps.Size(0, 400)
		});
		var con = $('#location2').html();
		var infowindow_2 = new google.maps.InfoWindow({
			content : con,
			maxWidth : 200,
			pixelOffset : new google.maps.Size(0, 400)
		});
		var con = $('#location3').html();
		var infowindow_3 = new google.maps.InfoWindow({
			content : con,
			maxWidth : 200,
			pixelOffset : new google.maps.Size(0, 400)
		});
		var con = $('#location4').html();
		var infowindow_4 = new google.maps.InfoWindow({
			content : con,
			maxWidth : 200,
			pixelOffset : new google.maps.Size(0, 400)
		});

		marker1.addListener('click', function() {
			google.maps.event.addListener(infowindow_1, 'domready', function() {

				// Reference to the DIV that wraps the bottom of infowindow
				var iwOuter = $('.gm-style-iw');

				/* Since this div is in a position prior to .gm-div style-iw.
				 * We use jQuery and create a iwBackground variable,
				 * and took advantage of the existing reference .gm-style-iw for the previous div with .prev().
				 */
				var iwBackground = iwOuter.prev();

				// Removes background shadow DIV
				iwBackground.children(':nth-child(2)').css({
					'display' : 'none'
				});

				// Removes white background DIV
				iwBackground.children(':nth-child(4)').css({
					'display' : 'none'
				});

				// Moves the infowindow 115px to the right.
				iwOuter.parent().parent().css({
					left : '80px'
				});

				// Moves the shadow of the arrow 76px to the left margin.
				iwBackground.children(':nth-child(1)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Moves the arrow 76px to the left margin.
				iwBackground.children(':nth-child(3)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Changes the desired tail shadow color.
				iwBackground.children(':nth-child(3)').find('div').children().css({
					'box-shadow' : 'rgba(72, 181, 233, 0) 0px 1px 6px',
					'z-index' : '1'
				});

				// Reference to the div that groups the close button elements.
				var iwCloseBtn = iwOuter.next();

				// Apply the desired effect to the close button
				iwCloseBtn.css({
					opacity : '1',
					right : '38px',
					top : '3px',
					border : 'none',
					'border-radius' : '0',
					'box-shadow' : '0 0 0 #3990B9'
				});

				// If the content of infowindow not exceed the set maximum height, then the gradient is removed.
				if ($('.iw-content').height() < 140) {
					$('.iw-bottom-gradient').css({
						display : 'none'
					});
				}
			});
			infowindow_1.open(map, marker1);

		});

		marker2.addListener('click', function() {
			google.maps.event.addListener(infowindow_2, 'domready', function() {

				// Reference to the DIV that wraps the bottom of infowindow
				var iwOuter = $('.gm-style-iw');

				/* Since this div is in a position prior to .gm-div style-iw.
				 * We use jQuery and create a iwBackground variable,
				 * and took advantage of the existing reference .gm-style-iw for the previous div with .prev().
				 */
				var iwBackground = iwOuter.prev();

				// Removes background shadow DIV
				iwBackground.children(':nth-child(2)').css({
					'display' : 'none'
				});

				// Removes white background DIV
				iwBackground.children(':nth-child(4)').css({
					'display' : 'none'
				});

				// Moves the infowindow 115px to the right.
				iwOuter.parent().parent().css({
					left : '80px'
				});

				// Moves the shadow of the arrow 76px to the left margin.
				iwBackground.children(':nth-child(1)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Moves the arrow 76px to the left margin.
				iwBackground.children(':nth-child(3)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Changes the desired tail shadow color.
				iwBackground.children(':nth-child(3)').find('div').children().css({
					'box-shadow' : 'rgba(72, 181, 233, 0) 0px 1px 6px',
					'z-index' : '1'
				});

				// Reference to the div that groups the close button elements.
				var iwCloseBtn = iwOuter.next();

				// Apply the desired effect to the close button
				iwCloseBtn.css({
					opacity : '1',
					right : '38px',
					top : '3px',
					border : 'none',
					'border-radius' : '0',
					'box-shadow' : '0 0 0 #3990B9'
				});

				// If the content of infowindow not exceed the set maximum height, then the gradient is removed.
				if ($('.iw-content').height() < 140) {
					$('.iw-bottom-gradient').css({
						display : 'none'
					});
				}
			});
			infowindow_2.open(map, marker2);

		});
		marker3.addListener('click', function() {
			google.maps.event.addListener(infowindow_3, 'domready', function() {

				// Reference to the DIV that wraps the bottom of infowindow
				var iwOuter = $('.gm-style-iw');

				/* Since this div is in a position prior to .gm-div style-iw.
				 * We use jQuery and create a iwBackground variable,
				 * and took advantage of the existing reference .gm-style-iw for the previous div with .prev().
				 */
				var iwBackground = iwOuter.prev();

				// Removes background shadow DIV
				iwBackground.children(':nth-child(2)').css({
					'display' : 'none'
				});

				// Removes white background DIV
				iwBackground.children(':nth-child(4)').css({
					'display' : 'none'
				});

				// Moves the infowindow 115px to the right.
				iwOuter.parent().parent().css({
					left : '80px'
				});

				// Moves the shadow of the arrow 76px to the left margin.
				iwBackground.children(':nth-child(1)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Moves the arrow 76px to the left margin.
				iwBackground.children(':nth-child(3)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Changes the desired tail shadow color.
				iwBackground.children(':nth-child(3)').find('div').children().css({
					'box-shadow' : 'rgba(72, 181, 233, 0) 0px 1px 6px',
					'z-index' : '1'
				});

				// Reference to the div that groups the close button elements.
				var iwCloseBtn = iwOuter.next();

				// Apply the desired effect to the close button
				iwCloseBtn.css({
					opacity : '1',
					right : '38px',
					top : '3px',
					border : 'none',
					'border-radius' : '0',
					'box-shadow' : '0 0 0 #3990B9'
				});

				// If the content of infowindow not exceed the set maximum height, then the gradient is removed.
				if ($('.iw-content').height() < 140) {
					$('.iw-bottom-gradient').css({
						display : 'none'
					});
				}
			});
			infowindow_3.open(map, marker3);

		});

		marker4.addListener('click', function() {
			google.maps.event.addListener(infowindow_4, 'domready', function() {

				// Reference to the DIV that wraps the bottom of infowindow
				var iwOuter = $('.gm-style-iw');

				/* Since this div is in a position prior to .gm-div style-iw.
				 * We use jQuery and create a iwBackground variable,
				 * and took advantage of the existing reference .gm-style-iw for the previous div with .prev().
				 */
				var iwBackground = iwOuter.prev();

				// Removes background shadow DIV
				iwBackground.children(':nth-child(2)').css({
					'display' : 'none'
				});

				// Removes white background DIV
				iwBackground.children(':nth-child(4)').css({
					'display' : 'none'
				});

				// Moves the infowindow 115px to the right.
				iwOuter.parent().parent().css({
					left : '80px'
				});

				// Moves the shadow of the arrow 76px to the left margin.
				iwBackground.children(':nth-child(1)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Moves the arrow 76px to the left margin.
				iwBackground.children(':nth-child(3)').attr('style', function(i, s) {
					return s + 'left: 76px !important;'
				});

				// Changes the desired tail shadow color.
				iwBackground.children(':nth-child(3)').find('div').children().css({
					'box-shadow' : 'rgba(72, 181, 233, 0) 0px 1px 6px',
					'z-index' : '1'
				});

				// Reference to the div that groups the close button elements.
				var iwCloseBtn = iwOuter.next();

				// Apply the desired effect to the close button
				iwCloseBtn.css({
					opacity : '1',
					right : '38px',
					top : '3px',
					border : 'none',
					'border-radius' : '0',
					'box-shadow' : '0 0 0 #3990B9'
				});

				// If the content of infowindow not exceed the set maximum height, then the gradient is removed.
				if ($('.iw-content').height() < 140) {
					$('.iw-bottom-gradient').css({
						display : 'none'
					});
				}
			});
			infowindow_4.open(map, marker4);

		});
	}

	//===============================
	if ($('#map-view1').length) {

		var pos = new google.maps.LatLng(41.236859, -73.667425);

		var map = new google.maps.Map(document.getElementById('map-view1'), {
			zoom : 16,
			center : pos,
			scrollwheel : false,
			mapTypeId : google.maps.MapTypeId.ROADMAP,
			streetViewControl : false,
			zoomControl : false,
			mapTypeControl : false
		});
		//map.mapTypes.set('map_style', styledMap);
		//map.setMapTypeId('map_style');

		var pos1 = new google.maps.LatLng(41.234200, -73.668000);

		var marker1 = new google.maps.Marker({
			position : pos1,
			map : map,
			draggable : false,
			icon : 'assets/images/map-marker.jpg'
		});

	}

});

