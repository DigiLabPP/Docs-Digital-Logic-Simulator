import os, json
static_dir = os.listdir(".\static")
fnames = []
temp = dict()
for i in static_dir:
    for j in os.listdir(f".\static\{i}"):
        name_file = (j.split(".")[0]).replace("_"," ")
        temp["name"] = f"{name_file}"
        j_n = j.replace(" ","_")
        temp["name_w"] = j_n.split(".")[0]
        os.rename(f".\static\{i}\{j}",f".\static\{i}\{j_n}")
        temp["url"] = f".\static\{i}\{j_n}"
        temp["loc"] = i
        fnames.append(str(temp))
        

''' 
    NOTE for Future work
    output comes like: [
        str(dict),....
    ]
    expected is [
        dict,....
    ]

    Cause of this issue: "\\" is getting converted to "\\\\"
    also dict is as string (which means 
    "{ => { 
        and 
    "} => }
    )

    make sure to convert the SdRd to S'R' (only in name)

'''

with open("gate_data.json","w") as f:
    json.dump(fnames,f,indent=4)