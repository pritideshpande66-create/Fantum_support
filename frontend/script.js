const chat = document.getElementById("chat");
const form = document.getElementById("chatForm");
const messageInput = document.getElementById("message");
const fileInput = document.getElementById("file");

function addMessage(text, cls) {
  const div = document.createElement("div");
  div.className = `msg ${cls}`;

  if (cls === "bot") {
    div.innerHTML = marked.parse(text); // markdown render
  } else {
    div.innerText = text;
  }

  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}
function quickAsk(text) {
  messageInput.value = text;
  form.requestSubmit();
}


form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const message = messageInput.value.trim();
  if (!message) return;

  addMessage(message, "user");

  const data = new FormData();
  data.append("message", message);

  if (fileInput.files.length > 0) {
    data.append("file", fileInput.files[0]);
  }

  try {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      body: data
    });

    const json = await res.json();
    
    addMessage(json.reply, "bot");
  } catch (err) {
    addMessage("Server error. Is backend running?", "bot");
    console.error(err);
  }

  form.reset();
});
