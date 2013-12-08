//Blatantly stolen from DJANGO docs
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }   
        }   
    }   
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }   
    }   
});

var req;

//Sends request to update status list
function sendRequest() {
    if (window.XMLHttpRequest){
        req = new XMLHttpRequest();
    } else {
        req = new ActiveXObject("Microsoft.XMLHTTP");
    }
    req.onreadystatechange = handleResponse;
    req.open("GET", "/titaniumfitness/get_list_home", true);
    console.log("ABOUT TO SEND REQUEST");
    req.send();
}

function handleResponse() {
    if (req.readyState != 4 || req.status != 200){
        return;
    }
    console.log("HOME STREAM HANDLE REQUEST");
    var xmlData = req.responseText;
    var list = document.getElementById("posted-statuses");
    var newContent = document.createElement("div");
    newContent.innerHTML = xmlData;
    
    var maxListID = $(list).find(".posted-status").attr('id'); 
    var maxContentID = $(newContent).find(".posted-status").attr('id');
    
    if (maxListID == undefined){
        maxListID = 0;
    }

    //Compares old content to new -- only grabs more recent statuses!
    var newStatuses = $(newContent).find(".posted-status").filter( function(){ 
        return (parseInt($(this).attr('id')) >  maxListID);
    })
    $(list).prepend(newStatuses.valueOf());
}

$(document).ready(function(){
    console.log("Fitness loaded");
    window.setInterval(sendRequest, 10000);
});
