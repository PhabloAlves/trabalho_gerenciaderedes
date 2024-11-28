const axios = require('axios');


const url = 'http://127.0.0.1:5000/converter';


const conversao = {
    criptomoeda: 'bitcoin', 
    moeda: 'usd',           
    quantidade: 1         
};


async function converterCriptomoeda() {
    try {
       
        const response = await axios.post(url, conversao);
        console.log('Resultado da conversão:', response.data);
    } catch (error) {
        console.error('Erro ao realizar conversão:', error.message);
    }
}


converterCriptomoeda();
