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

$(document).on('change', function() {
    $(".commentForm").submit(function(e) {
        var commentText = $(e.target).find("#commentText").val();
        if(commentText == "") return false;
        var statusID = $(e.target).find("#commentStatusID").val();
        var currentUrl = $(e.target).find("#commentCurrentUrl").val();
        var link = $(e.target).find("#commentLink").val();
        var name = $(e.target).find("#commentName").val();
        var src = $(e.target).find("#commentImgSrc").val();

        $(e.target).parent().parent().before('<div class="row-fluid comment"> <div class="span2"></div> <div class="row-fluid span10 well well-small"> <a href="' + link  +'"> <div class="span3">'+ name +'</div> <div class="span1"><img src="' + src + '" alt="' + name + '" class="img-polaroid comment-img" height="30" width="30"> </div> </a> <div class="span6"><p>' + commentText  + '</p></div><div class="span2"></div></div> </div>');
        $.ajax({
            url: "/titaniumfitness/add_comment",
            type: "POST", 
            data: { comment : commentText,  
                    statusID : statusID, 
                    currentUrl : currentUrl}
        }); 
        
        $(e.target).find("#commentText").val("");

        return false;
    });
});


$(document).ready(function(){
    $("#id_base_exercise").change(function(){
        var selectedNum = $(this).find(":selected").val();
        var selectedValue = $(this).find(":selected").text();
        var selectedClass = $(this).find(":selected").attr('class');
        if(selectedClass.indexOf("1") != -1){
            $("#id_reps").removeClass('hidden');
            $("#id_sets").removeClass('hidden');
        } else {
            $("#id_reps").addClass('hidden');
            $("#id_sets").addClass('hidden');
        }   
        if(selectedClass.indexOf("2") != -1){
            $("#id_weight").removeClass('hidden');
        } else {
            $("#id_weight").addClass('hidden');
        }   
        if(selectedClass.indexOf("3") != -1){
            $("#id_time").removeClass('hidden');
        } else {
            $("#id_time").addClass('hidden');
        }   
        if(selectedClass.indexOf("4") != -1){
            $("#id_distance").removeClass('hidden');
        } else {
            $("#id_distance").addClass('hidden');
        }   
    }); 
    
    $(".awesome").on('submit', function(e) {
        e.preventDefault();
        var statusID = $(this).find("[name='statusID']").val();
        var currentUrl = $(this).find("[name='currentUrl']").val();
        $.ajax({
            url: "/titaniumfitness/dislike",
            type: "POST", 
            data: { statusID : statusID,  
                    currentUrl : currentUrl}
        }); 
        
        $(e.target).find("[type='submit']").toggleClass("btn-info")
        $(e.target).find("[type='submit']").toggleClass("btn-success")
        
        var count = parseInt($(e.target).parent().children().first().children().first().html());

        if($(e.target).find("[type='submit']").val() == 'awesome'){
            $(e.target).find("[type='submit']").val('uncool'); 
            $(e.target).parent().children().first().children().first().html(count + 1);
        } else{
            $(e.target).find("[type='submit']").val('awesome'); 
            $(e.target).parent().children().first().children().first().html(count - 1);
        
        }
    });
    console.log("Comments loaded");
});

