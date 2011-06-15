(function(window, document, version, callback) {
	var j, d;
	var loaded = false;
	if (!(j = window.jQuery) || version > j.fn.jquery || callback(j)) {
		var script = document.createElement("script");
		script.type = "text/javascript";
		script.src = DEBUG_TOOLBAR_MEDIA_URL + "js/jquery.js";
		script.onload = script.onreadystatechange = function() {
			if (!loaded && (!(d = this.readyState) || d == "loaded" || d == "complete")) {
				callback((j = window.jQuery).noConflict(1), loaded = true);
				j(script).remove();
			}
		};
		document.documentElement.childNodes[0].appendChild(script)
	}
})(window, document, "1.3", function($, jquery_loaded){
	$(document).ready(function() {
		var prevBackToTopElem = null;
		$('#djDebug-htmlvalidator .handle-position').click(function(){
			$('#djDebug-htmlvalidator .repr-info-sel').removeClass('repr-info-sel');
			$(this).parent().parent().addClass('repr-info-sel');
			var text = $(this).text();
			var re = new RegExp('line\\s+([0-9]+)');
			var result = text.match(re);

			try{
				var lineno = result[1];
			}catch(e){return;}
			//
			var prevPos = $(document).data('reprlineselpos') || null;
			if(prevPos){
				prevPos.removeClass('repr-line-sel');
			}
			var reprLineElem = $('#djDebug-htmlvalidator .repr-line-' + lineno + ':first');
			reprLineElem.addClass('repr-line-sel');
			$(document).data('reprlineselpos', $('.repr-line-' + lineno));
			// skip pervious link and add new one

			var locationPrefix = location;
			if(location.href.indexOf('#') > -1){
				var newLocation = location.href.substring(0, location.href.indexOf('#'));
				locationPrefix = newLocation;
			}
			location = locationPrefix + '#' + 'repr-line-' + lineno;

			// add `back to top` functionality
			if(prevBackToTopElem){
			  prevBackToTopElem.remove();
			}
			var backToTopElem = $('#repr-line-backtotop').fadeOut('fast');

			var reprLineElemOffset = reprLineElem.offset();
			backToTopElem.css({
			  'top': reprLineElemOffset.top + 'px',
			  'left': (reprLineElemOffset.left - 17) + 'px'
			}).fadeIn('fast');
		});
		$('#djDebug-htmlvalidator .tidy-msg').click(function(e){
			$('.handle-position:first', $(this).prev()).click();
		});
	});
});