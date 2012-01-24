window.onload = function(){
    var todos = document.querySelectorAll('.todo');
    [].forEach.call(todos, function(todo) {
        todo.addEventListener('dragstart', handleDragStart, false);
        //todo.addEventListener('dragend', handleDragEnd, false);
    });       
};

function handleDragStart(e){
  this.style.opacity = "0.4";
};

function handleDragEnd(e){
    this.style.opacity = "1";
};