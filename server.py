import asyncio
import websockets
import json
from datetime import datetime
from aiohttp import web  # ✅ Move to top

connected_users = {}  # websocket: username
chat_log_file = "chat_log.json"

# Load chat history
try:
    with open(chat_log_file, "r") as f:
        chat_history = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    chat_history = []

def format_message(user, text):
    return {
        "time": datetime.now().strftime("%H:%M"),
        "user": user,
        "text": text
    }

def save_to_log(msg):
    chat_history.append(msg)
    with open(chat_log_file, "w") as f:
        json.dump(chat_history[-100:], f)

async def handler(websocket):
    try:
        username = await websocket.recv()

        if username in connected_users.values():
            await websocket.send(json.dumps(format_message("System", f"⚠️ '{username}' is already connected.")))
            await websocket.close()
            return

        connected_users[websocket] = username
        await notify_users(format_message("System", f"🟢 {username} joined the chat!"))

        for msg in chat_history:
            await websocket.send(json.dumps(msg))

        await notify_users(format_message("System", f"👥 Online: {', '.join(connected_users.values())}"))

        async for message in websocket:
            msg_text = message.strip()

            # 🧹 Only admin can clear chat
            if msg_text == "/clear" and username == "admin":
                chat_history.clear()
                with open(chat_log_file, "w") as f:
                    json.dump([], f)
                await notify_users(format_message("System", "🧹 Chat was cleared by admin."))
                continue

            msg = format_message(username, msg_text)
            print(f"[{username}]: {msg_text}")
            save_to_log(msg)
            await notify_users(msg)

    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        left_user = connected_users.pop(websocket, "Unknown")
        await notify_users(format_message("System", f"🔴 {left_user} left the chat."))

async def notify_users(message):
    if connected_users:
        await asyncio.gather(*(ws.send(json.dumps(message)) for ws in connected_users))

# ✅ Combined WebSocket + Frontend Server
async def start_server():
    # Serve static files
    app = web.Application()
    app.router.add_static("/", path="public", show_index=True)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 3000)
    await site.start()

    # Start WebSocket server
    await websockets.serve(handler, "0.0.0.0", 6789)
    print("✅ Server running at http://localhost:3000 and ws://localhost:6789")
    await asyncio.Future()

# ✅ Entry Point
if __name__ == "__main__":
    asyncio.run(start_server())
