chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
	chrome.tabs.executeScript({
			file: 'setup.js'
		});
	if(changeInfo.url.toString().startsWith("chrome")){ }
	else{ 
		var tablink;
		tablink = changeInfo.url.toString();
		var xhr=new XMLHttpRequest();
		var key = "vXSDrKoBvByAPkIzQIfQuiYDLx2OvH7wIypN67Mn";
		var markup = "key="+key+"&url="+tablink;
		xhr.open("POST","http://127.0.0.1:5000/api/v2/pishcheck",false);
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		xhr.send(markup);
		var data = JSON.parse(xhr.responseText);
		if(data.pish=="True"){
			// alert("Phishing Site");
			chrome.tabs.executeScript({file: 'phish.js'});
		}
		else if(data.pish == "False"){
			// alert("Safe site");
			chrome.tabs.executeScript({file: 'safe.js'});
		}
		else{
			alert("Oh ohh Unable to Predict");
		}
	}
 }); 