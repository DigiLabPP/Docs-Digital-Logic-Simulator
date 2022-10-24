import json

f = open("./static/gate_meta_data_new.json","w")
s = open("gate_data.json","r")

source_names = json.load(s)
# print(source_names)
meta_data = []
temp = {}
for i in source_names:
    meta_data.append({
        "name" : i["name"],
        "desc" : "",
        "truth_table" : "",
        "code" : "",
        "syntax" : ""
    })
# print(meta_data)

json.dump(meta_data,f,indent=4)

f.close()
s.close()