# 💬 TCPChatNet - Real-Time WebSocket Chat App

🚀 A fully functional, real-time WebSocket-based chat application built with Python (`aiohttp` + `websockets`), deployed on **Render**, and accessible from anywhere in the world.

🌐 **Live Demo**: [https://tcpchatnet.onrender.com](https://tcpchatnet.onrender.com)

---

## 📸 Preview

<!-- Replace with actual image URL -->
login page -
![image](https://github.com/user-attachments/assets/eb82abd9-4485-4d76-b161-4779337b0daa)

chat window- 
![image](https://github.com/user-attachments/assets/ad460003-3b9f-4788-9deb-bcbf076ee54f)

chatting -
![image](https://github.com/user-attachments/assets/452f0356-3cb1-4bc1-8cd7-aef1958426df)


---

## 🛠 Tech Stack

| Frontend       | Backend               | Protocols           | Deployment |
|----------------|------------------------|----------------------|------------|
| HTML, CSS, JS  | Python (`aiohttp`)     | TCP/IP, WebSocket, HTTP | Render     |
| Vanilla JS     | WebSockets (`asyncio`) |                      | GitHub     |

---

### 🔧 Architecture Overview
![ChatGPT Image Jun 14, 2025, 09_21_58 PM](https://github.com/user-attachments/assets/2c9c3a54-f7fc-411d-9d08-dce8fa84af63)

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

Developed with ❤️ by **[Siddharth Jagtap]**  
If you liked this project, ⭐ it and consider contributing!

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.
