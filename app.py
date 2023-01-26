from flask import Flask, render_template, url_for, redirect
import json

app = Flask(__name__)

def get_dict_data():
    f = open("gate_data.json","r")
    data = json.load(f)
    f.close()
    for i in data:
        i["imgloc"] = f"{i['loc']}/{i['name_w']}.svg"
    return data

@app.route('/')
def home_page():
    return render_template("homepage.html")


@app.route('/keywords/')
def keywords():
    return render_template("keywords.html")


@app.route('/keywords/<kw>/')
def delay_k(kw):
    status = {"delay":False,"control":False,"output":False,"simtime":False}
    if kw=="delay":
        status["delay"] = True
        return render_template("keyw_template.html",content=status)
    elif kw=="control":
        status["control"] = True
        return render_template("keyw_template.html",content=status)
    elif kw=="output":
        status["output"] = True
        return render_template("keyw_template.html",content=status)
    elif kw=="simtime":
        status["simtime"] = True
        return render_template("keyw_template.html",content=status)
    else:
        return redirect("/keywords/")


@app.route('/circuits/')
def circuits():
    return render_template("circuits.html")


@app.route('/circuits/gates/')
def cir_gates():
    gate_data = get_dict_data()
    return render_template("gates.html",gate_data=gate_data)


@app.route('/circuits/gates/<gate_name>/')
def gate_view(gate_name):
    gate_data = get_dict_data()
    gate = {}
    for i in gate_data:
        if i["name_w"] == gate_name:
            gate = i
            gate["loc"] = "cir_gates"
            gate["curr"] = "Simple Gates"
            gate["imgloc"] = f"Simple_gates/{i['name_w']}.svg"
            break
    f = open("./static/gate_meta_data.json","r")
    meta_data = json.load(f)
    f.close()
    for j in meta_data:
        if j["name"] == gate["name"]:
            gate = dict(gate,**j)
            break
    # print(gate)
    return render_template("circuit_template.html",gate_info=gate)


@app.route('/circuits/combinational/')
def cir_combi():
    gate_data = get_dict_data()
    return render_template("combinational.html",gate_data=gate_data)


@app.route('/circuits/combinational/<gate_name>/')
def combin_view(gate_name):
    gate_data = get_dict_data()
    gate = {}
    for i in gate_data:
        if i["name_w"] == gate_name:
            gate = i
            gate["loc"] = "cir_combi"
            gate["curr"] = "Combinational Circuits"
            gate["imgloc"] = f"Combinational_ckts/{i['name_w']}.svg"
            break
    f = open("./static/gate_meta_data.json","r")
    meta_data = json.load(f)
    f.close()
    for j in meta_data:
        if j["name"] == gate["name"]:
            gate["code"] = j["code"]
            gate["desc"] = j["desc"]
            gate["truth_table"] = j["truth_table"]
            break
    # print(gate)
    return render_template("circuit_template.html",gate_info=gate)


@app.route('/circuits/sequential/')
def cir_seq():
    gate_data = get_dict_data()
    return render_template("sequential.html",gate_data=gate_data)


@app.route('/circuits/sequential/<gate_name>/')
def seq_ckt_view(gate_name):
    gate_data = get_dict_data()
    gate = {}
    for i in gate_data:
        if i["name_w"] == gate_name:
            gate = i
            gate["loc"] = "cir_seq"
            gate["curr"] = "Sequential Circuits"
            gate["imgloc"] = f"Seq_ckts/{i['name_w']}.svg"
            break
    f = open("./static/gate_meta_data.json","r")
    meta_data = json.load(f)
    f.close()
    for j in meta_data:
        if j["name"] == gate["name"]:
            gate["code"] = j["code"]
            gate["desc"] = j["desc"]
            gate["truth_table"] = j["truth_table"]
            break
    # print(gate)
    return render_template("circuit_template.html",gate_info=gate)

@app.route('/aboutus/')
def about():
    return render_template("aboutus.html")

if __name__ == "__main__":
    app.run(debug=True)