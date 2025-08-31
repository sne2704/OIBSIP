import socket
from datetime import datetime # this is for timestamps
s = socket.socket()
# print("Socket made") not for user!
host = "127.0.0.1"
port = 12345
s.bind((host, port))
# print("Socket binded to", port)   # debugged
s.listen(1)
# print("Waiting for client...")   # Debugged
c, addr = s.accept()
# print("Connected with", addr)   # Debug info
# asking for name
your_name = input("Enter your name: ")
# sending the name to client
c.send(your_name.encode())
# receive client's name
friend_name = c.recv(1024).decode()
print(f"You are now chatting with {friend_name} ;)")
while True:
    data = c.recv(1024).decode()
    if not data:
        break
    if data.lower() == "bye":
        print(f"[{datetime.now().strftime('%H:%M')}] {friend_name} ended the chat.")
        break
    print(f"[{datetime.now().strftime('%H:%M')}] {friend_name}: {data}")
    msg = input(f"You: ")
    if msg.lower() == "bye":
        c.send(msg.encode())
        print(f"[{datetime.now().strftime('%H:%M')}] You ended the chat.")
        break
    c.send(msg.encode())
c.close()
