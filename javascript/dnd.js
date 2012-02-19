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
    
    new Droppable('donebasket', {
        ondrop: function (element) {
            var parentEl = element.parentElement;
            parentEl.removeChild(element);
            var todoidelement = getFirstElementByTagAndClassName("input", "todoid", parent=element);
            if(todoidelement && todoidelement.value){
                doSimpleXMLHttpRequest("http://" + HOST + "/setdone/" + todoidelement.value + "/");
            };
        }
    });
});