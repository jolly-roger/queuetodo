//var todos;
//
//window.onload = function(){
//    todos = document.querySelectorAll(".todo");
//    [].forEach.call(todos, function(todo) {
//        todo.addEventListener('dragstart', handleDragStart, false);
//        todo.addEventListener('dragenter', handleDragEnter, false);
//        todo.addEventListener('dragover', handleDragOver, false);
//        todo.addEventListener('dragleave', handleDragLeave, false);
//        todo.addEventListener('drop', handleDrop, false);
//        todo.addEventListener('dragend', handleDragEnd, false);
//    });
//    var donebaskets = document.querySelectorAll("#donebasket");
//    [].forEach.call(donebaskets, function(donebasket){
//        donebasket.addEventListener("drop", doneBasketDrop, false);
//        donebasket.addEventListener("dragover", doneBasketCancel, false);
//        donebasket.addEventListener("dragenter", doneBasketCancel, false);
//    });
//};
//
//function doneBasketCancel(e) {
//    if (e.preventDefault) e.preventDefault();
//    e.dataTransfer.dropEffect = 'move';
//    return false;
//};
//
//function doneBasketDrop(e){
//    if (e.stopPropagation) {
//        e.stopPropagation();
//    };
//
//    if (dragSrcEl != this) {
//        var parentEl = dragSrcEl.parentElement;
//        parentEl.removeChild(dragSrcEl);
//    };
//
//    return false;
//};
//
//var dragSrcEl = null;
//
//function handleDragStart(e) {
//  this.style.opacity = '0.4';
//
//  dragSrcEl = this;
//
//  e.dataTransfer.effectAllowed = 'move';
//  e.dataTransfer.setData('text/html', this);
//};
//
//function handleDrop(e) {
//  if (e.stopPropagation) {
//    e.stopPropagation();
//  };
//
//  if (dragSrcEl != this) {
//    var parentEl = dragSrcEl.parentElement;
//    parentEl.removeChild(dragSrcEl);
//    parentEl.insertBefore(dragSrcEl, this);
//  };
//
//  return false;
//};
//
//function handleDragEnd(e) {
//    this.style.opacity = "1";    
//    
//  [].forEach.call(todos, function (todo) {
//    todo.classList.remove('over');
//  });
//};
//
//function handleDragOver(e) {
//  if (e.preventDefault) {
//    e.preventDefault();
//  };
//
//  e.dataTransfer.dropEffect = 'move';
//
//  return false;
//};
//
//function handleDragEnter(e) {
//  this.classList.add('over');
//};
//
//function handleDragLeave(e) {
//  this.classList.remove('over');
//};


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