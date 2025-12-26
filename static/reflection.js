async function rephrase() {
    const text = document.getElementById("reflection-input").value;

    const response = await fetch("/ai_rephrase", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `text=${encodeURIComponent(text)}`
    });

    const data = await response.json();
    document.getElementById("ai-output").innerText = data.rephrased;
}
