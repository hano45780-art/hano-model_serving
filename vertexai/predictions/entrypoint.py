from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def health():
    return "OK", 200

@app.route("/predictions/model", methods=["POST"])
def predict():
    data = request.get_json()
    return jsonify({
        "predictions": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7080)