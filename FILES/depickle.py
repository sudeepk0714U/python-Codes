import json

f = open("example.txt","r")

d = json.load(f)
print(d)