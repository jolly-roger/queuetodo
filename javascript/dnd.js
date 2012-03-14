var SET_PRIORITY_URL = "http://" + HOST + "/setpriority/%(todoid)s/%(todopriority)s/";
var SHARE_URL = "http://" + HOST + "/share/%(todoid)s/%(friendid)s/";
var SET_STATUS_URL = "http://" + HOST + "/setstatus/%(todoid)s/%(statusid)s/";
var STATUS_FILTER_URL = "http://" + HOST + "/index/%(statusid)s/";

var TODO_ID = "%(todoid)s";
var TODO_PRIORITY = "%(todopriority)s";
var FRIEND_ID = "%(friendid)s";
var STATUS_ID = "%(statusid)s";


jQuery(document).ready(function(){
    var todos = getElementsByTagAndClassName("div", "todo");
    
    for(var i = 0; i < todos.length; i ++){
        new Draggable(todos[i], {revert: true});
        new Droppable(todos[i], {
            ondrop: (function(index){
                return function(element){
                    if(hasElementClass(element, "todo")){
                        var todoidelement = getFirstElementByTagAndClassName("input", "todoid", parent=element);
                        var newTodoPriorityElement = getFirstElementByTagAndClassName("input", "todoPriority",
                            parent=todos[index]);
                        var parentEl = element.parentElement;
                        
                        parentEl.removeChild(element);
                        parentEl.insertBefore(element, todos[index]);
                        
                        var url = (new String(SET_PRIORITY_URL)).
                            replace(TODO_ID, todoidelement.value).
                            replace(TODO_PRIORITY, newTodoPriorityElement.value);
                        
                        doSimpleXMLHttpRequest(url);
                    }else if(hasElementClass(element, "friend")){
                        var friendidelement = getFirstElementByTagAndClassName("input", "friendid", parent=element);
                        var todoidelement = getFirstElementByTagAndClassName("input", "todoid", parent=todos[index]);
                        
                        if(friendidelement && friendidelement.value && todoidelement && todoidelement.value){
                            var url = (new String(SHARE_URL)).
                                replace(TODO_ID, todoidelement.value).
                                replace(FRIEND_ID, friendidelement.value);
                            
                            doSimpleXMLHttpRequest(url);
                        };
                    }
                };
            })(i)
        });
        
        jQuery(todos[i]).find("select.statusSelector").change((function(index){
                return function(e){
                    var todoidelement = getFirstElementByTagAndClassName("input", "todoid", parent=todos[index]);
                    var url = (new String(SET_STATUS_URL)).
                        replace(TODO_ID, todoidelement.value).
                        replace(STATUS_ID, e.target.options[e.target.selectedIndex].value);
                    
                    doSimpleXMLHttpRequest(url);
                    removeElement(todos[index]);
                };
            })(i));
    };
    
    var friends = getElementsByTagAndClassName("div", "friend");
    for(var i = 0; i < friends.length; i ++){
        new Draggable(friends[i], {revert: true});
    };
    
    jQuery("#statusFilter").change(function(e){
        var url = (new String(STATUS_FILTER_URL)).
            replace(STATUS_ID, e.target.options[e.target.selectedIndex].value);
                        
        window.location = url;
    });
});


function addTodo(){
    jQuery.post("/addtodo", {todoname: jQuery("#todoName").val()});
};

    