(function($){
	$(document).ready(function() {
		var $htmlvalidator = $('#djDebug-htmlvalidator'),
			prevBackToTopElem = null;
		$htmlvalidator.find('.handle-position').click(function(){
			$htmlvalidator.find('.repr-info-sel').removeClass('repr-info-sel');
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
			var reprLineElem = $htmlvalidator.find('.repr-line-' + lineno + ':first');
			reprLineElem.addClass('repr-line-sel');
			$(document).data('reprlineselpos', $('.repr-line-' + lineno));
			// skip previous link and add new one

			var locationPrefix = window.location;
			if(window.location.href.indexOf('#') > -1){
				locationPrefix = window.location.href.substring(0, window.location.href.indexOf('#'));
			}
			window.location = locationPrefix + '#' + 'repr-line-' + lineno;

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
		$htmlvalidator.find('.tidy-msg').click(function(e){
			$('.handle-position:first', $(this).prev()).click();
		});
	});
}(jQuery));
