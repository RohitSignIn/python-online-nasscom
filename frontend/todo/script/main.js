$(document).ready(function () {
  const todoInput = document.getElementById("todoInput");
  const addTodo = document.getElementById("addTodoBtn");

  const todoCon = document.getElementById("todoCon");

  $.ajax({
    type: "get",
    url: "http://localhost:9090/api/v1/todos",
    success: function (response) {
      for (let i = 0; i < response["res"].length; i++) {
        console.log(response["res"][i][1]);
        addTodoInList(response["res"][i][1]);
      }
    },
  });

  function handleDelete(e) {
    e.target.parentElement.parentElement.remove();
  }

  todoInput.addEventListener("keyup", (event) => {
    if (event.code === "Enter") {
      addInputTodo();
    }
  });

  addTodo.addEventListener("click", addInputTodo);

  function addInputTodo() {
    $.ajax({
      type: "get",
      url: "http://localhost:9090/api/v1/todo",
      data: {
        task: todoInput.value,
        userId: 5,
      },
      success: function (response) {
        addTodoInList(todoInput.value);
      },
    });
  }

  function addTodoInList(task) {
    if (task == "") {
      return;
    }

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
  }
});
