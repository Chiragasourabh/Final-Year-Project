// alert(document.readyState);
if(document.readyState == "complete"){
	document.getElementById("safezfTvgE").click();
}
else{
	(function() {
	window.onload = function() {
        document.getElementById("safezfTvgE").click();
      };
})();
}

