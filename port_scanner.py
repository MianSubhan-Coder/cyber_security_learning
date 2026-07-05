import socket
target_host = "8.8.8.8"
ports_to_scan = [22, 53, 80, 443]

for port in ports_to_scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    try:
        s.connect(target_host, port)
        print(f"🟢 Port {port} is OPEN!")
    except:
        print(f"🔴 Port {port} is CLOSED.")
    finally:
        s.close()