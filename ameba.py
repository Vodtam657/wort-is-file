import json


with open("bd.json", "r") as file:
    b = json.load(file)

b.append(12)

with open("bd.json", "r", encoding="utf-8") as file:
    json.dump(b,file)

