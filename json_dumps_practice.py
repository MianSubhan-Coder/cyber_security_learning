import json

system_info = {
    "host": "Firewall-01",
    "ports": [22, 80],
    "monitored": True
}

json_string = json.dumps(system_info)

print(json_string)