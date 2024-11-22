function fare(event) {
    event.preventDefault();  // Impede o envio do formulário e o recarregamento da página
    const fareValue = document.getElementById('fare').value;
    
    if (fareValue !== '' && !isNaN(fareValue)) {
        const celso = (5 / 9) * (parseFloat(fareValue) - 32);
        window.alert(`${fareValue}° Fahrenheit é igual a ${celso.toFixed(2)}° Celsius.`);
    } else {
        window.alert('Por favor, insira um valor válido em Fahrenheit.');
    }
}

document.getElementById('formConversao').addEventListener('submit', fare);

function valorTotal(event) {
    event.preventDefault();

    const prodName = document.getElementById('nomeproduto').value;
    const prodQuant = parseFloat(document.getElementById('quanproduto').value);
    const prodUni = parseFloat(document.getElementById('unprod').value);
    const porcDesc = parseFloat(document.getElementById('porcdesc').value);

    // Verifica se os valores são válidos
    if (prodName !== '' && !isNaN(prodQuant) && !isNaN(prodUni) && !isNaN(porcDesc)) {
        let vT = prodQuant * prodUni;
        let vtP = vT * (porcDesc / 100);
        let vt = vT - vtP; 

        window.alert(`${prodName} foi comprado a R$${vt} (Desconto aplicado: R$${vtP.toFixed(2)}) [${prodQuant} unidades]`);
    } else {
        window.alert('Por favor, insira valores válidos.');
    }
}

document.getElementById('produto').addEventListener('submit', valorTotal);

function valorDolar(event) {
    event.preventDefault();

    const vReal = parseFloat(document.getElementById('real').value);
    const vCota = parseFloat(document.getElementById('cota').value);

    const vDolar = vReal / vCota

    window.alert(`Conversão de R$${vReal} para dólar: $${vDolar.toFixed(2)}`)
}

document.getElementById('dolar').addEventListener('submit', valorDolar);
