fetch("./dados.json").then(
    function resultado (resposta) {
        return resposta.json()
    }
).then(
    function(json) {
        const divPessoa = document.createElement('div');
        const paragrafo = document.createElement('p');
        const frase = `Meu nome é ${json.nome}, tenho ${json.idade} anos e sou ${json.profissão}`;

        paragrafo.innerText =  frase;
        divPessoa.appendChild(paragrafo);
        document.getElementById('app').appendChild(divPessoa);
    }
)