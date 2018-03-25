from flask import Flask, render_template, request
import returnCrop
app = Flask(__name__)

@app.route("/")
def input_data():
    return render_template("input.html")

@app.route("/results", methods = ['POST','GET'])
def results():
    state = (request.args["state"])
    area = (request.args["area"])
    capital = (request.args["capital"])
    (crop,ans,crops_possible) = returnCrop.returnCrop(state,area,capital)
    return render_template("result.html", crop=crop, ans=ans, area=area, crops_possible = crops_possible)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)