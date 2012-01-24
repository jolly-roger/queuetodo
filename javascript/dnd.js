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
  e.dataTransfer.setData('text/html', this);
};

function handleDrop(e) {
  if (e.stopPropagation) {
    e.stopPropagation();
  };

  if (dragSrcEl != this) {
    var parentEl = dragSrcEl.parentElement;
    parentEl.removeChild(dragSrcEl);
    parentEl.insertBefore(dragSrcEl, this);
  };

  return false;
};

function handleDragEnd(e) {
    this.style.opacity = "1";    
    
  [].forEach.call(todos, function (todo) {
    todo.classList.remove('over');
  });
};

function handleDragOver(e) {
  if (e.preventDefault) {
    e.preventDefault();
  };

  e.dataTransfer.dropEffect = 'move';

  return false;
};

function handleDragEnter(e) {
  this.classList.add('over');
};

function handleDragLeave(e) {
  this.classList.remove('over');
};