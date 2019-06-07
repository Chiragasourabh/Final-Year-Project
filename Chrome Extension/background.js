function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
		tablink = tab.url;
		// swal("Congrats!", ", Your account is created!", "success");
		var xhr=new XMLHttpRequest();
		var key = "vXSDrKoBvByAPkIzQIfQuiYDLx2OvH7wIypN67Mn";
		var markup = "key="+key+"&url="+tablink;
		// alert(markup);
		xhr.open("POST","http://127.0.0.1:5000/api/v2/pishcheck",false);
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send(markup);
		// alert(xhr.responseText);
		var data = JSON.parse(xhr.responseText);
		if(data.pish=="True"){
			// alert("Phishing Site");
			alert("Phishing Site");
		}
		else if(data.pish == "False"){
			// alert("Safe site");
			alert("Safe site");
			// swal("Safe site!", "You can move forward!", "success")
		}
		else{
			alert("Oh ohh Unable to Predict");
		}
	});
}

chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
	// alert("Hello");
	transfer();
 }); 