const token =
    localStorage.getItem("access");

let editingTaskId = null;

async function loadTasks(){

    const response = await fetch(
        "http://127.0.0.1:8000/api/tasks/fetch_or_create/",
        {
            headers:{
                Authorization:
                    `Bearer ${token}`
            }
        }
    );

    const tasks = await response.json();

    let html = "";

    tasks.forEach(task => {

        html += `
            <div class="card mb-2">

                <div class="card-body">

                    <h5>${task.title}</h5>

                    <p>${task.description}</p>
                    <button
                        class="btn btn-warning me-2"
                        onclick="editTask(${task.id},
                                        '${task.title}',
                                        '${task.description}')">

                        Edit

                    </button>

                    <button
                        class="btn btn-danger"
                        onclick="deleteTask(${task.id})">

                        Delete

                    </button>

                </div>

            </div>
        `;
    });

    document.getElementById("tasks").innerHTML =
        html;
}

loadTasks();

function editTask(id, title, description){

    editingTaskId = id;

    document.getElementById("title").value =
        title;

    document.getElementById("description").value =
        description;

    document.getElementById("createBtn").innerText =
        "Update Task";
}


async function createTask(){

    const title =
        document.getElementById("title").value;

    const description =
        document.getElementById("description").value;
        
    if(editingTaskId){

        await updateTask(
            editingTaskId,
            title,
            description
        );

        return;
    }

    const response = await fetch(
        "http://127.0.0.1:8000/api/tasks/fetch_or_create/",
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json",

                Authorization:
                    `Bearer ${token}`
            },

            body: JSON.stringify({
                title,
                description
            })
        }
    );

    if(response.ok){

        alert("Task Created Successfully!");

        loadTasks();
    }
}


async function deleteTask(id){

    const response = await fetch(
        `http://127.0.0.1:8000/api/tasks/fetch_create_update/${id}/`,
        {
            method: "DELETE",

            headers:{
                Authorization:
                    `Bearer ${token}`
            }
        }
    );

    if(response.ok){

        alert("Task Deleted Successfully!");

        loadTasks();
    }

    else{

        alert("Failed to delete task!");
    }
}

async function updateTask(
    id,
    title,
    description
){

    const response = await fetch(
        `http://127.0.0.1:8000/api/tasks/fetch_create_update/${id}/`,
        {
            method:"PATCH",

            headers:{
                "Content-Type":"application/json",

                Authorization:
                    `Bearer ${token}`
            },

            body: JSON.stringify({
                title,
                description
            })
        }
    );

    if(response.ok){

        alert("Task Updated Successfully!");

        editingTaskId = null;

        document.getElementById("createBtn")
            .innerText = "Create Task";

        document.getElementById("title").value =
            "";

        document.getElementById("description").value =
            "";

        loadTasks();
    }
}