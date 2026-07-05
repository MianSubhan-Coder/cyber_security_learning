import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2.0)

s.connect(("8.8.8.8", 53))
print("🔗 Connection successful! Port 53 is OPEN.")
s.close()