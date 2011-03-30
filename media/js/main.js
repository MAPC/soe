$(document).ready(function() {	
	
	// hide all the sub-menus
	// $("h4.toggle").next().hide();
	
	// set the cursor of the toggling elements
	// $("h4.toggle").css("cursor", "pointer");
	
	// prepend a plus sign to signify that the sub-menus aren't expanded
	// $("h4.toggle").prepend("+ ");
	
	// the active menu
	// $("h4.active").next().toggle();
	
	// add a click function that toggles the sub-menu when the corresponding
	// span element is clicked
	/* 
	$("h4.toggle").click(function() {
		$(this).next().toggle(500);
	}); 
	*/
	
	// fix height
	if ($("#content").height() < $(window).height()) { 
		$("#content").height($(window).height()); 
	}
	
	// lightbox effect: 
	$("a.graph").lightBox();
	
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