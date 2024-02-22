let data = {
  username: "Rohit",
};

$.ajax({
  type: "get",
  url: "http://localhost:9090/api/v1/todos",
  success: function (response) {
    // console.log(response);
    for (let i = 0; i < response["res"].length; i++) {
      paintUI(response["res"][i][1]);
    }
  },
});

let status = document.getElementById("persona");

let addTodo = document.getElementById("addTodo");
let todoInput = document.getElementById("todoInput");
let todoCon = document.getElementById("todoCon");

addTodo.addEventListener("click", () => {
  // todoInput.value
  // Check how to convert in FormData

  //   $.ajax({
  //     type: "POST",
  //     url: "http://localhost:9090/api/v1/todos",
  //     data: ,
  //     success: function (response) {
  //       paintUI(todoInput.value);
  //     },
  //   });

  paintUI(todoInput.value);
});

function paintUI(task) {
  todo = document.createElement("div");
  todoPara = document.createElement("p");
  btnCon = document.createElement("div");
  statusBtn = document.createElement("button");
  deleteBtn = document.createElement("button");

  todo.classList.add("d-flex");
  todo.classList.add("gap-2");
  todoPara.classList.add("flex-grow-1");
  todoPara.classList.add("border");
  todoPara.classList.add("p-2");

  todoPara.textContent = task;

  statusBtn.classList.add("btn");
  statusBtn.classList.add("btn-warning");
  statusBtn.textContent = "Completed";

  deleteBtn.classList.add("btn");
  deleteBtn.classList.add("ms-2");
  deleteBtn.classList.add("btn-danger");
  deleteBtn.textContent = "Delete";

  btnCon.appendChild(statusBtn);
  btnCon.appendChild(deleteBtn);

  todo.appendChild(todoPara);
  todo.appendChild(btnCon);

  todoCon.appendChild(todo);
}
