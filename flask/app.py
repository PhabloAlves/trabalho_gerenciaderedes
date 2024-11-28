from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


def buscar_preco(criptomoeda, moeda):
    url = "https://api.coingecko.com/api/v3/simple/price"
    parametros = {
        "ids": criptomoeda,
        "vs_currencies": moeda
    }
    resposta = requests.get(url, params=parametros)
    if resposta.status_code == 200:
        return resposta.json()
    return None


@app.route('/converter', methods=['POST'])
def converter():
    dados = request.json
    criptomoeda = dados.get('criptomoeda') 
    moeda = dados.get('moeda') 
    quantidade = dados.get('quantidade', 1)  

    precos = buscar_preco(criptomoeda, moeda)
    if not precos or criptomoeda not in precos or moeda not in precos[criptomoeda]:
        return jsonify({"erro": "Criptomoeda ou moeda inválida"}), 400

    taxa_conversao = precos[criptomoeda][moeda]
    valor_convertido = quantidade * taxa_conversao

    return jsonify({
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "quantidade": quantidade,
        "taxa_conversao": taxa_conversao,
        "valor_convertido": f"{valor_convertido:,.2f}"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
