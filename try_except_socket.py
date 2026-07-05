import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect(("8.8.8.8", 999))
    s.settimeout(1.0)
    print("Port is open")
except:
    s.settimeout(1.0)
    print("Port is closed or timed out")
finally:
    s.settimeout(1.0)
    s.close()