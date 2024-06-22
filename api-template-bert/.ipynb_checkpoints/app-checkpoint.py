import platform
import pickle
import torch
import os
import requests

from flask import Flask, jsonify, request
from flask_cors import CORS
from transformers import BertTokenizer, BertForSequenceClassification

# ////////////////////////////////////////////////////////////////////////
# TODO: Adjust the code part below
# ////////////////////////////////////////////////////////////////////////

GROUP_ID = 'predictive-pandas' # TODO: Replace with your groupID
MODEL_FILE = 'bert.model' # relative path to your model file
MODEL_VERSION = 'v0.3'

# TODO: Adjust the function below so that it calls your vectorizer and 
# classifier functions packaged in the .model file.
def batch_predict(items):    
    # Load the saved model and tokenizer
    model_path = 'model_files'
    tokenizer = BertTokenizer.from_pretrained(model_path)
    model = BertForSequenceClassification.from_pretrained(model_path)

    print(items)

    # Ensure the model is in evaluation mode
    model.eval()

    # Example text for sentiment classification
    texts = [item['text'] for item in items]
    ids = [item['id'] for item in items]
    
    # Tokenize the input texts
    inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True, max_length=128)

    # Run inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the predicted class
    predictions = torch.argmax(outputs.logits, dim=-1)

    print("TYPE ", type(predictions))
    mapping = {0: -1, 1: 0, 2: 1}
    results = []
    for idt, prediction in zip(ids, predictions):
        print("TEST", idt, " ", prediction.item())
        print(type(prediction.item()))
        results.append({
            "id": idt,
            "label": mapping[prediction.item()],
        })
        
    return results


files_to_download = [
    ("https://predictive-pandas.s3.eu-north-1.amazonaws.com/bert/config.json", "config.json"),
    ("https://predictive-pandas.s3.eu-north-1.amazonaws.com/bert/vocab.txt", "vocab.txt"),
    ("https://predictive-pandas.s3.eu-north-1.amazonaws.com/bert/special_tokens_map.json", "special_tokens_map.json"),
    ("https://predictive-pandas.s3.eu-north-1.amazonaws.com/bert/model.safetensors", "model.safetensors"),
    ("https://predictive-pandas.s3.eu-north-1.amazonaws.com/bert/tokenizer_config.json", "tokenizer_config.json")
]

def download_files(file_list, directory):
    print("TEST !!!222")
    for url, filename in file_list:
        local_filename = os.path.join(directory, filename)
        if os.path.exists(local_filename):
            print(f'{local_filename} already exists. Skipping download.')
            continue
        try:
            print("TEST !!!22211, ", url, " ", local_filename)
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes
            with open(local_filename, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded {local_filename}')
        except requests.RequestException as e:
            print(f'Failed to download {filename} from {url}. Error: {e}')

# ////////////////////////////////////////////////////////////////////////
# You should not modify the code below.
# ////////////////////////////////////////////////////////////////////////

app = Flask(__name__) # set up app
CORS(app) # set up CORS policies

# # load model file
# with open(MODEL_FILE, 'rb') as file:
#     model = pickle.load(file)
local_dir = 'model_files'
os.makedirs(local_dir, exist_ok=True)

download_files(files_to_download, local_dir)

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
        print("TEST", items)
        return jsonify({ "items": batch_predict(items) }) # batch predictions
    else:
        return jsonify({"meta": meta_data}) # meta data

# start the api server when running the script
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)