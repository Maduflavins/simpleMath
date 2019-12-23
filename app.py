from flask import Flask, jsonify, request
from flask_restful import Api, Resource



app = Flask("__name__")

api = Api(app)
def checkReqData(reqData, functionName):
    if(functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in reqData or "y" not in reqData:
            return 301
        else:
            return 200
    elif(functionName == "divide"):
        if "x" not in reqData or "y" not in reqData:
            return 301
        elif int(reqData["y"])==0:
            return 302
        else:
            return 200
        
    
class Add(Resource):
    def post(self):
        reqData = request.get_json()

        status_code = checkReqData(reqData, "add")
        if(status_code != 200):
            retJson = {
                        "Message": "An error occured",
                        "Status Code" : status_code

                    }
            return jsonify(retJson)

        
        x = reqData["x"]
        y = reqData["y"]
        x = int(x)
        y = int(y)
        ret = x + y
        retmap = {
                    "Message" : ret,
                    "Status Code": 200

                }
        return jsonify(retmap)
class Subtract(Resource):
    def post(self):
        reqData = request.get_json()
        status_code = checkReqData(reqData, "subtract")
        if(status_code!=200):
            retJson={
                "Message": "An error occured",
                "Status Code": status_code
            }
            return jsonify(retJson)
        

        x = reqData["x"]
        y = reqData["y"]
        x = int(x)
        y = int(y)
        ret = x - y
        retmap = {
            "Message": ret,
            "Status Code": 200
        }
        return jsonify(retmap)
    


class Multiply(Resource):
    def post(self):
        reqData = request.get_json()
        status_code = checkReqData(reqData, "multiply")
        if(status_code!=200):
            retJson={
                "Message": "An error occured",
                "Status Code": status_code
            }

            return jsonify(retJson)
        

        x = reqData["x"]
        y = reqData["y"]
        x = int(x)
        y = int(y)
        ret = x * y

        retmap = {
            "Message": ret,
            "Status Code": 200
        }
        return jsonify(retmap)


class Divide(Resource):
    def post(self):
        reqData = request.get_json()
        status_code = checkReqData(reqData, "divide")
        if(status_code!=200):
            retJson={
                "Message": "An error occured",
                "Status Code": status_code
            }
            return jsonify(retJson)
        
        x = reqData["x"]
        y = reqData["y"]
        x = int(x)
        y = int(y)
        ret = (x*1.0) / y
        retmap = {
            "Message": ret,
            "Status Code" : 200
        }
        return jsonify(retmap)

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app.route("/")
def hell_world():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
