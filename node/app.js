const axios = require('axios');


const url = 'http://127.0.0.1:5000/jogadores';


async function getJogadores() {
    try {
        const response = await axios.get(url);
        console.log('Jogadores:', response.data);
    } catch (error) {
        console.error('Erro ao listar jogadores:', error.message);
    }
}



getJogadores();  
