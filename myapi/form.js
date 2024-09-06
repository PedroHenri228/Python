document.addEventListener('DOMContentLoaded', () => {
    var form = document.getElementById("myform");
    var erroMessage = document.getElementById("errorMessage");

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        var text1 = document.getElementById('text1').value;
        var text2 = document.getElementById('text2').value;

        // Verifica se os campos estão preenchidos
        if (text1 === '' || text2 === '') {
            erroMessage.textContent = 'Por favor, preencha todos os campos';
            return;
        }

        erroMessage.textContent = ''; // Limpa a mensagem de erro

        alert('Formulário enviado com sucesso! Texto 1: ' + text1 + ' Texto 2: ' + text2);

        // Enviar dados para o servidor
        fetch('/save_json', {
            method: 'POST',
            body: JSON.stringify({ text1: text1, text2: text2 }),
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Erro:', error));
    });
});
