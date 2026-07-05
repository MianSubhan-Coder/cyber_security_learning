url = input("Enter the URL to scan: ")
bugs = int(input("Enter the number of bugs found in the web: "))
print(f"Scanning {url}... Found {bugs} critical vulnerabilities.")
if bugs > 0:
    print("🔴 Alert! Threat detected. Secure the system immediately!")
else:
    print("🟢 System clean. No vulnerabilities found.")