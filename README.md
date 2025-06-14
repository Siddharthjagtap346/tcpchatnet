# 💬 TCPChatNet - Real-Time WebSocket Chat App

🚀 A fully functional, real-time WebSocket-based chat application built with Python (aiohttp + websockets), deployed on **Render**, and accessible from anywhere in the world.

🌐 **Live Demo**: [https://tcpchatnet.onrender.com](https://tcpchatnet.onrender.com)

---

## 📸 Preview

![Chat UI Preview](https://your-image-url-if-any.com/preview.png)

---

## 🛠 Tech Stack

| Frontend      | Backend             | Deployment |
|---------------|---------------------|------------|
| HTML, CSS, JS | Python (aiohttp)    | Render     |
| Vanilla JS    | Websockets (asyncio)| GitHub     |

---

## 📁 Project Structure

tcpchatnet/
├── public/
│ ├── index.html # Chat UI
│ ├── styles.css # Styling
│ ├── chat.js # WebSocket logic
│ └── sounds/ # Optional sounds
├── chat_log.json # Stores last 100 messages
├── server.py # Python backend (WebSocket + HTTP)
└── README.md # This file


---

## 🚀 Features

✅ Real-time messaging  
✅ Dynamic user join/leave announcements  
✅ Scrollable chat log  
✅ Typing indicator (simulated)  
✅ Message persistence  
✅ Admin `/clear` command  
✅ Online user count  
✅ Color-coded avatars  
✅ Disconnection alerts  
✅ Fully deployed on the internet (Render)

---

## 🧪 How to Run Locally

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/tcpchatnet.git
cd tcpchatnet

### 2. Install dependencies

pip install aiohttp

### 3. Run the server
python server.py

### 4. Visit in your browser
Go to: http://localhost:3000
---

## 🌍 Live Deployment (Render)
Already deployed and live ✅
Access: https://tcpchatnet.onrender.com

### Steps (in case you want to redeploy):
#### 1. Push code to GitHub

#### 2. Link your repo on Render

Use these settings:

Start Command: python server.py

Port: 3000

Root Directory: Leave blank if server.py is in root

Render detects and exposes both HTTP:3000 (site) and HTTP:6789 (WebSocket)

#### ⚙️ Environment & Notes
Works on any modern browser

Default WebSocket port: 6789

Backend serves both frontend files and WebSocket handler

chat_log.json stores up to 100 messages for persistence

---

## ✨ Future Enhancements
✅ Typing indicator bubbles

🔒 Authentication / login system

📥 Downloadable chat history

📱 Responsive mobile UI

🔔 Desktop notifications

🌐 Internationalization support

🙌 Credits
Developed with ❤️ by [Your Name]
If you liked this project, ⭐ it and consider contributing!

## 📜 License
This project is licensed under the MIT License. See LICENSE for details.

---

✅ Let me know your GitHub username so I can adjust the `git clone` link and author credit if needed. Also, if you want preview images or badges (build passing, MIT license, etc.), I can include those too.

Would you like a `LICENSE` file and `.gitignore` file too?
