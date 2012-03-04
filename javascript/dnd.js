addLoadEvent(function(){
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
                        doSimpleXMLHttpRequest("http://" + HOST + "/setpriority/" + todoidelement.value + "/" +
                            newTodoPriorityElement.value + "/");
                    }else if(hasElementClass(element, "friend")){
                        var friendidelement = getFirstElementByTagAndClassName("input", "friendid", parent=element);
                        var todoidelement = getFirstElementByTagAndClassName("input", "todoid", parent=todos[index]);
                        if(friendidelement && friendidelement.value && todoidelement && todoidelement.value){
                            doSimpleXMLHttpRequest("http://" + HOST + "/share/" + todoidelement.value + "/" +
                                friendidelement.value + "/");
                        };
                    }
                };
            })(i)
        });
        var statusSelector = getFirstElementByTagAndClassName("select", "statusSelector", parent=todos[i]);
        if(statusSelector){
            statusSelector.onchange = (function(index){
                return function(e){
                    var todoidelement = getFirstElementByTagAndClassName("input", "todoid", parent=todos[index]);
                    doSimpleXMLHttpRequest("http://" + HOST + "/setstatus/" + todoidelement.value + "/" +
                    e.target.options[e.target.selectedIndex].value + "/");
                    removeElement(todos[index]);
                };
            })(i);
        };
    };
    
    var friends = getElementsByTagAndClassName("div", "friend");
    for(var i = 0; i < friends.length; i ++){
        new Draggable(friends[i], {revert: true});
    };
    
    $("statusFilter").onchange = function(e){
        window.location = "http://" + HOST + "/index/" + e.target.options[e.target.selectedIndex].value + "/";
    };
});