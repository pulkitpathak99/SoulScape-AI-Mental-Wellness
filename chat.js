document.getElementById("send-btn").addEventListener("click", () => {
    const userInput = document.getElementById("user-input").value.trim();
    if (!userInput) return;

    // Add user's message to the chatbox
    addMessage("user", userInput);
    document.getElementById("user-input").value = ""; // Clear input field

    // Send the user input to the server
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    })
        .then((response) => response.json())
        .then((data) => {
            // Add AI response to the chatbox
            addMessage("ai", data.response);

            // If a mood is detected and it's not neutral, show activity suggestion
            if (data.mood && data.activity_url && data.mood !== "Neutral") {
                displayActivitySuggestion(data.mood, data.activity, data.activity_url);
            }
        })
        .catch((error) => console.error("Error:", error));
});

function addMessage(sender, text) {
    const chatBox = document.getElementById("chat-box");
    const message = document.createElement("div");
    message.classList.add("message", sender);
    message.innerHTML = `<p>${text}</p>`;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
}

function displayActivitySuggestion(mood, activity, activityUrl) {
    const chatBox = document.getElementById("chat-box");
    const suggestion = document.createElement("div");
    suggestion.classList.add("activity-suggestion");

    // Display the suggestion only if the mood is not a neutral
    suggestion.innerHTML = `
        <p>We’ve detected you're feeling <strong>${mood}</strong>.</p>
        <p>Would you like to try the <strong>${activity}</strong> activity?</p>
        <button onclick="window.location.href='${activityUrl}'">Go to Activity</button>
    `;

    chatBox.appendChild(suggestion);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to show suggestion
}





