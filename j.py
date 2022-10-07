import json
f = open('sampledata.json')
data = json.load(f)
for i in data:
    print(i)
  
f.close()