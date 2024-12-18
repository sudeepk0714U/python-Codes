import json
f = open("example.txt","w")
d = {"satt" : 30,"dld" : 30,"pdenm":30}
json.dump(d,f)
f.close()