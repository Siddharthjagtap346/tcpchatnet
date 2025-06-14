let ws;
let username = null;

const chatBox = document.getElementById("chat-box");
const input = document.getElementById("msg-input");
const sendBtn = document.getElementById("send-btn");

const loginBtn = document.getElementById("login-btn");
const loginInput = document.getElementById("username-input");
const loginScreen = document.getElementById("login-screen");
const chatScreen = document.getElementById("chat-screen");

function stringToColor(str) {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = str.charCodeAt(i) + ((hash << 5) - hash);
  }
  return `hsl(${hash % 360}, 80%, 50%)`;
}

function addMessage(msg) {
  removeTypingBubble();

  const div = document.createElement("div");
  div.className = "message";
  const avatarColor = stringToColor(msg.user || "System");

  div.innerHTML = `
    <div class="avatar" style="background-color: ${avatarColor}">
      ${msg.user ? msg.user[0].toUpperCase() : "!"}
    </div>
    <div class="bubble">
      <div class="meta">
        <span class="name">${msg.user}</span>
        <span class="time">${msg.time}</span>
      </div>
      <div class="text">${msg.text}</div>
    </div>
  `;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTypingBubble() {
  if (document.getElementById("typing-bubble")) return;

  const typingDiv = document.createElement("div");
  typingDiv.className = "message typing";
  typingDiv.id = "typing-bubble";

  typingDiv.innerHTML = `
    <div class="avatar" style="background-color: #00ff88;">…</div>
    <div class="bubble">
      <div class="meta">
        <span class="name">System</span>
        <span class="time">typing…</span>
      </div>
      <div class="typing-dots">
        <span></span><span></span><span></span>
      </div>
    </div>
  `;
  chatBox.appendChild(typingDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTypingBubble() {
  const typing = document.getElementById("typing-bubble");
  if (typing) typing.remove();
}

function sendMessage() {
  const text = input.value.trim();
  if (text && ws && ws.readyState === WebSocket.OPEN) {
    ws.send(text);
    input.value = "";
  }
}

function connect(name) {
  username = name;
  ws = new WebSocket("wss://tcpchatnet.onrender.com");

  ws.onopen = () => {
    ws.send(username);
  };

  ws.onmessage = (event) => {
    try {
      const msg = JSON.parse(event.data);
      if (msg.text && msg.text.includes("already connected")) {
        alert("⚠️ That username is already in use.");
        ws.close();
        disableChat();
        return;
      }

      // 🟢 Play message sound only if message is not from self
      const receiveSound = document.getElementById("msg-receive-sound");
      if (msg.user !== username && receiveSound) receiveSound.play();

      showTypingBubble();
      setTimeout(() => addMessage(msg), 300); // Delay for realism
    } catch (e) {
      console.error("Invalid JSON from server", e);
    }
  };

  ws.onclose = () => {
    addMessage({
      time: new Date().toLocaleTimeString(),
      user: "System",
      text: "🔌 Disconnected from server."
    });
    disableChat();
  };
}

function disableChat() {
  input.disabled = true;
  sendBtn.disabled = true;
  loginInput.disabled = false;
  loginBtn.disabled = false;
}

// 👇 Login logic on button click
loginBtn.onclick = () => {
  const name = loginInput.value.trim();
  if (!name || name.length < 2) {
    alert("❌ Username must be at least 2 characters.");
    return;
  }

  const loginSound = document.getElementById("login-sound");
  if (loginSound) loginSound.play();

  loginScreen.style.display = "none";
  chatScreen.style.display = "block";
  chatScreen.classList.add("active");

  connect(name);
};

sendBtn.onclick = (e) => {
  e.preventDefault();
  sendMessage();
};

input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    sendMessage();
  }
});
