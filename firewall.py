blocked_users = ["attacker99", "malware_bot", "bad_actor"]
user = input("Enter username to log in: ")
if user in blocked_users:
    print("❌ Connection Refused. Account banned by Firewall.")
else:
    print("🔓 Connection Successful. Welcome to the secure network.")