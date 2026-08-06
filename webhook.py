from flask import Flask,request

app = Flask(__name__)


@app.route("/callback",methods=["POST"])
def callback():

    data=request.json

    print(data)

    return "OK"

if __name__ == "__main__":
    app.run(port=5000)