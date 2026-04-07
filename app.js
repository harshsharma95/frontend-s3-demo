document.getElementById("contactForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value
    };

    const msg = document.getElementById("msg");
    msg.innerText = "⏳ Sending...";

    try {
        const res = await fetch("https://lu8jfxlu30.execute-api.ap-south-1.amazonaws.com/prod/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        msg.innerText = result.message;
        msg.style.color = "lightgreen";

    } catch (error) {
        msg.innerText = "⚠️ Backend not connected!";
        msg.style.color = "red";
    }
});
