import os
import json
import asyncio
from datetime import datetime
from aiohttp import web

connected_users = {}  # websocket -> username
chat_history = []

chat_log_file = "chat_log.json"

# Load old chats
try:
    with open(chat_log_file, "r") as f:
        chat_history = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    chat_history = []

# Format message
def format_message(user, text):
    return {
        "time": datetime.now().strftime("%I:%M:%S %p"),
        "user": user,
        "text": text
    }

# Save to log file
def save_to_log(msg):
    chat_history.append(msg)
    with open(chat_log_file, "w") as f:
        json.dump(chat_history[-100:], f)

# WebSocket Handler
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    username = await ws.receive_str()

    # Username conflict
    if username in connected_users.values():
        await ws.send_json(format_message("System", f"⚠️ Username '{username}' already connected."))
        await ws.close()
        return ws

    connected_users[ws] = username

    # Announce join
    await broadcast(format_message("System", f"🟢 {username} joined the chat!"))

    # Send old chat
    for msg in chat_history:
        await ws.send_json(msg)

    # Online users
    await broadcast(format_message("System", f"👥 Online: {', '.join(connected_users.values())}"))

    try:
        async for msg in ws:
            text = msg.data.strip()

            if text == "/clear" and username == "admin":
                chat_history.clear()
                with open(chat_log_file, "w") as f:
                    json.dump([], f)
                await broadcast(format_message("System", "🧹 Chat cleared by admin."))
                continue

            chat_msg = format_message(username, text)
            save_to_log(chat_msg)
            await broadcast(chat_msg)

    except Exception:
        pass
    finally:
        left = connected_users.pop(ws, "Unknown")
        await broadcast(format_message("System", f"🔴 {left} left the chat."))

    return ws

# Broadcast message to all users
async def broadcast(msg):
    dead = []
    for ws in connected_users:
        try:
            await ws.send_json(msg)
        except:
            dead.append(ws)

    # Clean disconnected clients
    for ws in dead:
        connected_users.pop(ws, None)

# Main app setup
async def start_app():
    app = web.Application()
    app.router.add_static("/", path="public", show_index=True)
    app.router.add_get("/ws", websocket_handler)
    return app

# Entrypoint
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    web.run_app(start_app(), port=port)
