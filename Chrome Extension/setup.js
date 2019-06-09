(function() {
	var buttonOne = document.createElement('button');
	buttonOne.style.position = 'fixed';
	buttonOne.style.top = 0;
    buttonOne.style.right = 0;
    buttonOne.id = "safezfTvgE";
    buttonOne.innerHTML = "Safe";
    buttonOne.style.visibility = "hidden";
    buttonOne.setAttribute('onclick', "swal('Safe', 'Good to go!', 'success')");
    document.body.appendChild(buttonOne);
    
    var buttonTwo = document.createElement('button');
	buttonTwo.style.position = 'fixed';
	buttonTwo.style.top = 0;
    buttonTwo.style.left = 0;
    buttonTwo.id = "phishzfTvgE";
    buttonTwo.innerHTML = "Danger";
    buttonTwo.style.visibility = "hidden";
    buttonTwo.setAttribute('onclick', "swal('Deceptive Web Content Detected', 'Do not give your credentials!!', 'error')");
	document.body.appendChild(buttonTwo);

    var script = document.createElement('script');
    script.src = 'https://unpkg.com/sweetalert/dist/sweetalert.min.js';
    document.head.appendChild(script);

    var node = document.createElement('style');
	node.innerHTML = 'body { font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif; }';
	document.body.appendChild(node);

})();