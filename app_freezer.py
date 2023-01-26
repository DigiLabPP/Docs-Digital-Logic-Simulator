from flask_frozen import Freezer
from app import app
import json

app.config["FREEZER_RELATIVE_URLS"] = True
freezer = Freezer(app)

@freezer.register_generator
def generator():
    # keywords
    yield "/keywords/delay/"
    yield "/keywords/control/"
    yield "/keywords/output/"
    yield "/keywords/simtime/"

    # rest circuits
    f = open("./gate_data.json","r")
    gate_data = json.load(f)
    f.close()
    for i in gate_data:
        # print(i)
        if i["loc"] == "Combinational_ckts":
            yield f"/circuits/combinational/{i['name_w']}/"
        elif i["loc"] == "Seq_ckts":
            yield f"/circuits/sequential/{i['name_w']}/"
        elif i["loc"]=="Simple_gates":
            yield f"/circuits/gates/{i['name_w']}/"

if __name__ == '__main__':
    freezer.freeze()