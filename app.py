from flask import Flask, request, jsonify
from Bio import SeqIO
from flask_cors import CORS
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = Flask(__name__)


CORS(app) 
def read_fasta(file_path):
    sequences = []
    labels = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))
        labels.append(record.id)
    return sequences, labels
def one_hot_encode(sequences):
    encoding_dict = {'A': [1, 0, 0, 0],
                     'C': [0, 1, 0, 0],
                     'G': [0, 0, 1, 0],
                     'T': [0, 0, 0, 1]}
    encoded_sequences = []
    for seq in sequences:
        encoded_seq = []
        for char in seq:
            encoded_seq.extend(encoding_dict.get(char, [0, 0, 0, 0]))
        encoded_sequences.append(encoded_seq)
    return np.array(encoded_sequences)
def train_model(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
    model = SVC()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

fasta_file = "./sequance.txt"

sequences, labels = read_fasta(fasta_file)
features = one_hot_encode(sequences)
model, accuracy = train_model(features, labels)

@app.route('/classify', methods=['POST'])
def classify_sequence():
    data = request.get_json()
    sequence = data['sequence']

    encoded_sequence = one_hot_encode([sequence])
    result = model.predict(encoded_sequence)

    return jsonify({'result': result[0]})

if __name__ == '__main__':
    app.run(debug=True)
