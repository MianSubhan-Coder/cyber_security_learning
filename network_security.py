banned_ips = ["192.168.1.5", "10.0.0.7", "172.16.0.2"]

ip_address = input("Enter your IP address: ")

if ip_address in banned_ips:
    print("🚨 Access Denied! Banned IP address.")

else:
    print("✅ IP verified. Proceeding to password authentication...")

    for i in range(3):
        password = input("Enter the password: ")

        if password == 'cyber2026':
            print("🔓 System Access Granted. Welcome, Admin.")
            break
        else:
            print("❌ Incorrect password.")

            if i == 2:
                print("🔒 THREAT DETECTED: System locked down due to multiple failed logins!")
