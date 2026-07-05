target_ip = "192.168.8.8"
port = 80
ports_to_scan = [22, 80, 443]

print(f"Target IP is: {target_ip}")
if port == 80:
    print("Standard Web Port Detected.")
else:
    print("Alternative Service Port")

for ports in ports_to_scan:
    print(f"Auditing_port: {ports}")