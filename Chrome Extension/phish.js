// alert(document.readyState);
if(document.readyState == "complete"){
	document.getElementById("phishzfTvgE").click();
}
else{
	(function() {
    window.onload = function() {
        document.getElementById("phishzfTvgE").click();
      };
})();
}
