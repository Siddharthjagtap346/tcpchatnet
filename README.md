# 💬 TCPChatNet - Real-Time WebSocket Chat App

🚀 A fully functional, real-time WebSocket-based chat application built with Python (`aiohttp` + `websockets`), deployed on **Render**, and accessible from anywhere in the world.

🌐 **Live Demo**: [https://tcpchatnet.onrender.com](https://tcpchatnet.onrender.com)

---

## 📸 Preview

<!-- Replace with actual image URL -->
![Chat UI Preview](https://your-image-url-if-any.com/preview.png)

---

## 🛠 Tech Stack

| Frontend       | Backend               | Deployment |
|----------------|------------------------|------------|
| HTML, CSS, JS  | Python (`aiohttp`)     | Render     |
| Vanilla JS     | WebSockets (`asyncio`) | GitHub     |

---

## 📁 Project Structure

```
tcpchatnet/
├── public/
│   ├── index.html         # Chat UI
│   ├── styles.css         # Styling
│   ├── chat.js            # WebSocket logic
│   └── sounds/            # Optional sounds
├── chat_log.json          # Stores last 100 messages
├── server.py              # Python backend (WebSocket + HTTP)
└── README.md              # Project documentation
```

---

## 🚀 Features

- ✅ Real-time messaging  
- ✅ Dynamic user join/leave announcements  
- ✅ Scrollable chat log  
- ✅ Typing indicator (simulated)  
- ✅ Message persistence  
- ✅ Admin `/clear` command  
- ✅ Online user count  
- ✅ Color-coded avatars  
- ✅ Disconnection alerts  
- ✅ Fully deployed on the internet (Render)

---

## 🧪 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/tcpchatnet.git
cd tcpchatnet
```

### 2. Install dependencies

```bash
pip install aiohttp
```

### 3. Run the server

```bash
python server.py
```

### 4. Visit in your browser

Go to: [http://localhost:3000](http://localhost:3000)

---

## 🌍 Live Deployment (Render)

The app is already deployed and live ✅  
🔗 Access it here: [https://tcpchatnet.onrender.com](https://tcpchatnet.onrender.com)

### To Redeploy:

1. Push your code to GitHub  
2. Link your GitHub repo on [Render](https://render.com)

**Render Settings:**

- **Start Command:** `python server.py`  
- **Port:** `3000`  
- **Root Directory:** Leave blank if `server.py` is in the root  
- Render will expose:
  - HTTP (Frontend): `3000`
  - WebSocket: `6789`

### ⚙️ Environment & Notes

- Compatible with all modern browsers  
- Default WebSocket port: `6789`  
- `chat_log.json` stores up to 100 messages for persistence  
- The backend serves both frontend static files and WebSocket logic  

---

## ✨ Future Enhancements

- ✅ Typing indicator bubbles  
- 🔒 Authentication / login system  
- 📥 Downloadable chat history  
- 📱 Responsive mobile UI  
- 🔔 Desktop notifications  
- 🌐 Internationalization support  

---

## 🙌 Credits

Developed with ❤️ by **[Your Name]**  
If you liked this project, ⭐ it and consider contributing!

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
