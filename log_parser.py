with open("network.log", "r") as file:
    for line in file:
        cleaned_line = line.strip()

        if "CRITICAL" in cleaned_line:
            print(f"🚨 SECURITY BREACH FOUND -> {cleaned_line}")
            with open("compromised_hosts.txt", "a") as output_file:
                output_file.write(cleaned_line + "\n")
        elif "WARN" in cleaned_line:
            print(f"⚠️ SUSPICIOUS ACTIVITY -> {cleaned_line}")