addLoadEvent(function(){
    var todos = getElementsByTagAndClassName("div", "todo");
    for(var i = 0; i < todos.length; i ++){
        new Draggable(todos[i], {revert: true});
        new Droppable(todos[i], {
            ondrop: (function(index){
                return function(element){
                    if(hasElementClass(element, "todo")){
                        var parentEl = element.parentElement;
                        parentEl.removeChild(element);
                        parentEl.insertBefore(element, todos[index]);
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
    };
    
    var friends = getElementsByTagAndClassName("div", "friend");
    for(var i = 0; i < friends.length; i ++){
        new Draggable(friends[i], {revert: true});
    };
    
    var statusSelectors = getElementsByTagAndClassName("select", "statusSelector");
    for(var i = 0; i < statusSelectors.length; i ++){
        statusSelectors[i].onchange = function(e){
            alert("Yo!!!");
        };
    };
});