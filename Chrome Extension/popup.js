function transfer(){	
	var tablink;
	chrome.tabs.getSelected(null,function(tab) {
	   	tablink = tab.url;
		$("#p1").text("The URL being tested is - "+tablink);
		var xhr=new XMLHttpRequest();
		var key = "vXSDrKoBvByAPkIzQIfQuiYDLx2OvH7wIypN67Mn";
		var markup = "key="+key+"&url="+tablink;
		// alert(markup);
		xhr.open("POST","http://127.0.0.1:5000/api/v2/pishcheck",false);
		xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
		//xhr.onreadystatechange = checkData;
		xhr.send(markup);
function checkData()
{
    alert(xhr.readyState);
}

		// alert(xhr.responseText);
		var data = JSON.parse(xhr.responseText);
		if(data.pish=="True"){
			// alert("Phishing Site");
			$("#info").text("Phishing Site");
			$("#info").css("color", "red");
			$("#image").css('background-image', 'url(/red.jpg)');
		}
		else if(data.pish == "False"){
			// alert("Safe site");
			$("#info").text("Safe site");
			$("#info").css("color", "green");
			$("#image").css('background-image', 'url(/green.jpg)');
		}
		else{
			alert("Oh ohh Unable to Predict");
		}
		// $("#info").text(xhr.responseText);
		// return xhr.responseText;
		$("#loading").removeClass("fa fa-spinner fa-spin");
	});
}


$(document).ready(function(){
    $("#button").click(function(){	
			$("#loading").addClass("fa fa-spinner fa-spin");
			
			transfer();
			
    });
});

f

// chrome.tabs.getSelected(null,function(tab) {
//    	var tablink = tab.url;
// 	$("#p1").text("The URL being tested is - "+tablink);
// });


// chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
// 	// alert(changeInfo.url);
// 	transfer();
//  }); 