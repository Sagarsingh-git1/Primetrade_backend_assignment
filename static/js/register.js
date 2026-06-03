async function registerUser() {

    const username =
        document.getElementById("username").value.trim();

    const email =
        document.getElementById("email").value.trim();

    const password =
        document.getElementById("password").value.trim();

    const messageDiv =
        document.getElementById("message");

    if (!username || !email || !password) {

        messageDiv.innerHTML =
            "All fields are required.";

        return;
    }

    const response = await fetch(
        "http://127.0.0.1:8000/api/accounts/register/",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                username,
                email,
                password
            })
        }
    );

    const data = await response.json();

    if (response.ok) {

        messageDiv.innerHTML =
            "Registration successful! Redirecting to login...";

        setTimeout(() => {

            window.location.href = "/login/";

        }, 1500);
    }

    else {

        messageDiv.innerHTML =
            JSON.stringify(data);
    }
}