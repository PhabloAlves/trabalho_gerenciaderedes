import json
from flask import Flask, jsonify, request

app = Flask(__name__)

dados = [{'id': 1, 'nome': 'Joao Silva'},
         {'id': 2, 'nome': 'Cristiano Ronaldo'},
         {'id': 3, 'nome': 'Lionel Messi'}]


nextId = 4


@app.route('/jogadores', methods=['GET'])
def get_jogadores():
    return jsonify(dados)


@app.route('/jogadores', methods=['POST'])
def create_jogadores():
    global nextId
    novo_jogador = request.get_json() 
    novo_jogador['id'] = nextId  
    dados.append(novo_jogador)
    nextId += 1  
    return jsonify(novo_jogador), 201 

@app.route('/jogadores/<int:id>', methods=['PUT'])
def update_jogador(id):
    jogador_atualizado = request.get_json() 
    for jogador in dados:
        if jogador['id'] == id:
            jogador['nome'] = jogador_atualizado['nome'] 
            return jsonify(jogador) 
    return jsonify({'error': 'Jogador não encontrado'}), 404  

@app.route('/jogadores/<int:id>', methods=['DELETE'])
def delete_jogador(id):
    for jogador in dados:
        if jogador['id'] == id:
            dados.remove(jogador)
            return jsonify({'message': 'Jogador excluído com sucesso'}), 200  
    return jsonify({'error': 'Jogador não encontrado'}), 404 

if __name__ == '__main__':
    app.run(debug=True)
