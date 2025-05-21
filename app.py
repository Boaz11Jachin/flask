# pip install flask
# pip install numpy
# pip install pandas
# pip install flask-cors
# pip install prophet sqlalchemy pysql

# flask 실행시키려면, 터미널에 flask run
from flask import Flask, request
from flask_cors import CORS
from flask_cors import cross_origin
import util
import util2
import predict

app = Flask(__name__)
CORS(app, origins="*")   # api 전체

@app.get("/api/health" )
@cross_origin() # 라우트마다
def health_handle() :
    return {"status" : True}

@app.get("/api/hospital/groups")
def hospital_groups_handle() :
    response = util.count_hospital_type()
    print(response)
    return response, 200

@app.get("/api/health-info")
def health_info() :
    response = util2.drink()

    return response

@app.get("/api/predict/<region>")
def predict_handle(region) :
    df = predict.load_region_data(region)
    result = predict.run_prophet(df)
    to_dict = result.to_dict()

    xlabels = [v  for v in to_dict["ds"].values() ]
    data = [v for v in to_dict["yhat"].values() ]

    return { "xlabels" : xlabels, "data" : data }, 200



