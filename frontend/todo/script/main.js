const todoInput = document.getElementById("todoInput");
const addTodo = document.getElementById("addTodoBtn");

const todoCon = document.getElementById("todoCon");

function handleDelete(e) {
  e.target.parentElement.parentElement.remove();
}

addTodo.addEventListener("click", function () {
  const task = todoInput.value;

  const para = document.createElement("p");
  para.textContent = task;

  const statusBtn = document.createElement("button");
  statusBtn.textContent = "PENDING";
  statusBtn.classList.add("btnDel");

  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "DELETE";
  deleteBtn.classList.add("btnPend");

  paraCon = document.createElement("div");
  statusCon = document.createElement("div");
  deleteCon = document.createElement("div");

  paraCon.append(para);
  statusCon.append(statusBtn);
  deleteCon.append(deleteBtn);

  taskCon = document.createElement("div");
  taskCon.append(paraCon);
  taskCon.append(statusCon);
  taskCon.append(deleteCon);
  taskCon.classList.add("todo");

  todoCon.append(taskCon);

  todoInput.value = "";

  // Event Listeners
  deleteCon.addEventListener("click", (e) => handleDelete(e));
});
