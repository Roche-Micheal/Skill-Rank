import json


with open('C:\\Users\\hp\\OneDrive\\Desktop\\skill rank\\Assessment-2\\ex5.json', 'r') as openfile:
    j = json.load(openfile)
 
# print(j)

res = { "id": "1003", "type" : "tea" }

for d in j:
    if(d["name"] == "Old Fashioned"):
        r = d["batters"]["batter"]
        r.append(res.copy())
        with open('C:\\Users\\hp\\OneDrive\\Desktop\\skill rank\\Assessment-2\\ex5_updated.json', "w", encoding="ANSI") as file:
            json.dump(j, file, indent = 6)
            print(j)

    

