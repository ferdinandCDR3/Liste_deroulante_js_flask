from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def traiter_champ_texte():
    donnees = request.get_json()
    return donnees

if __name__ == '__main__':
    app.run()