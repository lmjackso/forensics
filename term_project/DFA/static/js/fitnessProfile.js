var req;

//Sends request to update status list
function sendRequest() {
    if (window.XMLHttpRequest){
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.onreadystatechange = handleResponse;
    req.open("GET", "/titaniumfitness/get_list_profile", true);
    console.log("ABOUT TO SEND REQUEST");
    req.send();
}

function handleResponse() {
    if (req.readyState != 4 || req.status != 200){
        return;
    }
    console.log("USER PROFILE HANDLE REQUEST"); 
    var xmlData = req.responseText;
    var list = document.getElementById("posted-statuses");
    var newContent = document.createElement("div");
    newContent.innerHTML = xmlData;
    
    var maxListID = $(list).find(".posted-status").attr('id'); 
    var maxContentID = $(newContent).find(".posted-status").attr('id');

    if(maxListID == undefined){
        maxListID = 0;
    }

    //Compares old content to new -- only grabs more recent statuses!
    var newStatuses = $(newContent).find(".posted-status").filter( function(){ 
        return (parseInt($(this).attr('id')) > maxListID);
    })


    $(list).prepend(newStatuses.valueOf());
}

window.setInterval(sendRequest, 10000);
