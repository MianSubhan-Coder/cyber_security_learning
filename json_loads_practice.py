import json

raw_string = '{"target": "Server-A", "active": true}'

data = json.loads(raw_string)

print(data["target"])