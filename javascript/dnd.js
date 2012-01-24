window.onload = function(){
    var todos = document.querySelectorAll('.todo');
    [].forEach.call(todos, function(todo) {
        todo.addEventListener('dragstart', handleDragStart, false);
        todo.addEventListener('dragenter', handleDragEnter, false);
        todo.addEventListener('dragover', handleDragOver, false);
        todo.addEventListener('dragleave', handleDragLeave, false);
    });       
};

function handleDragStart(e){
  this.style.opacity = "0.4";
};

function handleDragEnd(e){
    this.style.opacity = "1";
};

function handleDragOver(e) {
  if (e.preventDefault) {
    e.preventDefault(); // Necessary. Allows us to drop.
  }

  e.dataTransfer.dropEffect = 'move';  // See the section on the DataTransfer object.

  return false;
};

function handleDragEnter(e) {
  // this / e.target is the current hover target.
  this.addClassName('over');
}

function handleDragLeave(e) {
  this.removeClassName('over');  // this / e.target is previous target element.
}