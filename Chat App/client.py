import socket
from datetime import datetime
s = socket.socket()
# print("Socket created")   # Debugged
host = "127.0.0.1"
port = 12345
s.connect((host, port))
# print("Connected to server")   # Debugged
# ask for your name
your_name = input("Enter your name: ")
# receiving server's name first
friend_name = s.recv(1024).decode()
# sending name back
s.send(your_name.encode())
print(f"You are now chatting with {friend_name} ;)")

while True:
    msg = input(f"You: ")
    if msg.lower() == "bye":
        s.send(msg.encode())
        print(f"[{datetime.now().strftime('%H:%M')}] You ended the chat.")
        break
    s.send(msg.encode())

    data = s.recv(1024).decode()
    if data.lower() == "bye":
        print(f"[{datetime.now().strftime('%H:%M')}] {friend_name} ended the chat.")
        break
    print(f"[{datetime.now().strftime('%H:%M')}] {friend_name}: {data}")

s.close()
