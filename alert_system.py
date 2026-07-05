with open("alert.txt", "w") as file:
    file.write("INSTRUCTION DETECTED\n")

with open("alert.txt", "a") as file:
    file.write("SOURCE: Unknown\n")