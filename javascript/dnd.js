var todos;

window.onload = function(){
    todos = document.querySelectorAll('.todo');
    [].forEach.call(todos, function(todo) {
        todo.addEventListener('dragstart', handleDragStart, false);
        todo.addEventListener('dragenter', handleDragEnter, false);
        todo.addEventListener('dragover', handleDragOver, false);
        todo.addEventListener('dragleave', handleDragLeave, false);
        todo.addEventListener('drop', handleDrop, false);
        todo.addEventListener('dragend', handleDragEnd, false);
    });       
};

var dragSrcEl = null;

function handleDragStart(e) {
  this.style.opacity = '0.4';

  dragSrcEl = this;

  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', this.innerHTML);
}

function handleDrop(e) {
  // this / e.target is current target element.

  if (e.stopPropagation) {
    e.stopPropagation(); // stops the browser from redirecting.
  }

  // See the section on the DataTransfer object.

  return false;
}

function handleDragEnd(e) {
  // this/e.target is the source node.

  [].forEach.call(todos, function (todo) {
    todo.classList.removeClassName('over');
  });
}

function handleDragOver(e) {
  if (e.preventDefault) {
    e.preventDefault(); // Necessary. Allows us to drop.
  }

  e.dataTransfer.dropEffect = 'move';  // See the section on the DataTransfer object.

  return false;
};

function handleDragEnter(e) {
  // this / e.target is the current hover target.
  this.classList.addClassName('over');
}

function handleDragLeave(e) {
  this.classList.removeClassName('over');  // this / e.target is previous target element.
}