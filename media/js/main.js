$(document).ready(function() {	
	
	// fix height
	if ($("#main").height() < $(window).height()) { 
		$("#main").height($(window).height()); 
	}
	
	// lightbox on graphs 
	$("a.graph").lightBox();
	
	// mouseover event on all graphs
	// shows "click to enlarge" hint
	$("a.graph img").mouseover(function() {
		
		var $graphhint = $("<div class='graphhint'>click to enlarge</div>");
		
		$("#imagecol").append($graphhint);
		
		$graphhint
		.width($(this).width())
		.css({
			"background": "#004990",
			"color": "#fff",
			"opacity": "0.8",
			"font-size": "16px",
			"text-align": "center"})
		.position({
			my: "left top",
			at: "left top",
			of: this,
			collision: "fit"
		});	
			
		$(this).mouseout(function() {
		
			$graphhint.remove();
		
		});
	});
	
	// learn more
	$(".learnmoretxt").hide();
	$(".learnmore").click(function() {
		$(this).parent().next().toggle(500);
		// $(this).hide();
	});
	
	$(".learnmore").toggle(function() {
		$(this).html("Collapse text...");
	}, function() {
		$(this).html("Learn more...");
	});
	
	// find and correct reference links	
	$("a[href*='/reference/']").attr("href", function() {
		
		// FIXME: use something like this.href.replace("reference", "references");
		url = this.href.split("/");
		reference = url.pop();
		
		this.href = SOE.base_url + "references/" + reference;
		
	});
	
});