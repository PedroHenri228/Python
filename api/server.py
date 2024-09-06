from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/save_json', methods=['POST'])
def save_json():
    # Obter dados JSON da requisição
    data = request.json
    
    # Salvar dados em um arquivo JSON
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    # Ler o arquivo JSON e retornar o conteúdo
    with open('data.json', 'r') as file:
        saved_data = json.load(file)
    
    return jsonify(saved_data)

@app.route('/api', methods=['GET', 'POST'])
def get_api():
    if request.method == 'POST':
        data = request.json
        text1 = data.get('text1', '')
        text2 = data.get('text2', '')
        response_data = {'text1': text1, 'text2': text2}
    else:
        response_data = {'message': 'Send a POST request to /api with text1 and text2'}
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
