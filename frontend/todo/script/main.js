const todoInput = document.getElementById("todoInput");
const addTodo = document.getElementById("addTodoBtn");

const todoCon = document.getElementById("todoCon");

addTodo.addEventListener("click", function () {
  const task = todoInput.value;

  const para = document.createElement("p");
  para.textContent = task;

  const statusBtn = document.createElement("button");
  statusBtn.textContent = "PENDING";
  statusBtn.classList.add("btnPend");

  const deleteBtn = document.createElement("button");
  deleteBtn.textContent = "DELETE";
  statusBtn.classList.add("btnDel");

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

  // <div class='todo'>
  //   <div>
  //     <p>Task ...</p>
  //   </div>
  //   <div>
  //     <button class='btnPend'>PENDING</button>
  //   </div>
  //   <div>
  //     <button class='btnDel'>DELETE</button>
  //   </div>
  // </div>;
});
