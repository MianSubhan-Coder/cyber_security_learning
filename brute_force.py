for i in range(5):
    password = input("Enter password attempt: ")
    if password == 'admin123':
        print("🔓 Access Granted! Welcome back.")
        break
    else:
        print("❌ Wrong password. Trying next combination...")
