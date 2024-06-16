import platform
import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS


# ////////////////////////////////////////////////////////////////////////
# TODO: Adjust the code part below
# ////////////////////////////////////////////////////////////////////////

GROUP_ID = 'benchmarking-beaver' # TODO: Replace with your groupID
MODEL_FILE = 'benchmark.model' # relative path to your model file
MODEL_VERSION = 'v0.1'

# TODO: Adjust the function below so that it calls your vectorizer and 
# classifier functions packaged in the .model file.
def batch_predict(model, items):
    results = []
    for item in items:
        X = model['vectorizer'].fit_transform([item['text']])
        label = model['classifier'].predict(X)
        results.append({
            "id": item['id'],
            "label": int(label[0]),
        })
    return results


# ////////////////////////////////////////////////////////////////////////
# You should not modify the code below.
# ////////////////////////////////////////////////////////////////////////

app = Flask(__name__) # set up app
CORS(app) # set up CORS policies

# load model file
with open(MODEL_FILE, 'rb') as file:
    model = pickle.load(file)

# define meta-data for API
meta_data = {
    "groupID": GROUP_ID,
    "modelFile": MODEL_FILE,
    "modelVersion": MODEL_VERSION,
    "pythonVersion": platform.python_version()
}

# api route
@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        items = request.json['items']
        return jsonify({ "items": batch_predict(model, items) }) # batch predictions
    else:
        return jsonify({"meta": meta_data}) # meta data

# start the api server when running the script
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)