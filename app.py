from flask import Flask, request, jsonify
from collections import OrderedDict
import json

app = Flask(__name__)


@app.get("/")
def get_countries():
    return {"message" : "Hello World"}


@app.post("/bhfl")
def post_request():
    if request.is_json:
        data = request.get_json()
        _list = data['data']
        temp=json.loads(json.dumps(_list))
        _num_list = []
        _alpha_list= []
        success = True
        for i in temp:
            if str(i).isalnum():
                if str(i).isdigit():
                    _num_list.append(int(i))
                else:
                    _alpha_list.append(i)
       
        od  = OrderedDict({
            "is_success": "true",
            "user_id": "Tushar_Sharma_26_02_2000)",
            "email": "tusharsharmaci19@acropolis.in",
            "roll_number": "0827CI191059",
            "numbers": json.dumps(_num_list),
            "alphabets": _alpha_list
        })
        return  od
         
    return {"is_success": False}


if __name__ == '__main__':
    app.run(debug=True)