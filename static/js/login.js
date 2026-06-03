async function loginUser() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const response = await fetch(
        "http://127.0.0.1:8000/api/accounts/login/",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username: username,
                password: password
            })
        }
    );

    const data = await response.json();

    if(response.ok){

        localStorage.setItem(
            "access",
            data.access
        );

        localStorage.setItem(
            "refresh",
            data.refresh
        );

        window.location.href = "/dashboard/";
    }

    else{

        document.getElementById("message").innerHTML =
            "Invalid Credentials!";
    }
}