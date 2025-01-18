// Carrega o mapa salvo em mapa_realista.json e o renderiza no Canvas.
window.onload = function() {
    const canvas = document.getElementById('mapCanvas');
    const ctx = canvas.getContext('2d');
    const tamanhoTile = 2; // Define o tamanho de cada tile no Canvas.

    // Faz uma requisição para carregar o arquivo mapa_realista.json.
    fetch('mapa_realista.json')
        .then(response => response.json())
        .then(dadosMapa => {
            // Ajusta o tamanho do Canvas com base nas dimensões do mapa.
            canvas.width = dadosMapa[0].length * tamanhoTile;
            canvas.height = dadosMapa.length * tamanhoTile;

            // Itera sobre cada célula do mapa e desenha o tile correspondente.
            for (let y = 0; y < dadosMapa.length; y++) {
                for (let x = 0; x < dadosMapa[y].length; x++) {
                    desenharTile(ctx, x, y, dadosMapa[y][x], tamanhoTile);
                }
            }
        })
        .catch(err => console.error('Erro ao carregar o mapa:', err));
};

// Função que desenha cada tile no Canvas com base no tipo.
function desenharTile(ctx, x, y, tipo, tamanho) {
    switch (tipo) {
        case 'floresta':
            ctx.fillStyle = 'green';
            break;
        case 'deserto':
            ctx.fillStyle = 'yellow';
            break;
        case 'planícies':
            ctx.fillStyle = 'lightgreen';
            break;
        case 'pântano':
            ctx.fillStyle = 'darkgreen';
            break;
        case 'bosque':
            ctx.fillStyle = '#228B22'; // Verde floresta.
            break;
        case 'rio':
            ctx.fillStyle = 'blue';
            break;
        case 'montanha':
            ctx.fillStyle = 'gray';
            break;
        case 'colina':
            ctx.fillStyle = '#A9A9A9'; // Cinza claro.
            break;
        case 'estrada de terra':
            ctx.fillStyle = '#8B4513'; // Marrom terra.
            break;
        case 'estrada de calcamento':
            ctx.fillStyle = '#695473'; // Rosa claro.
            break;
        case 'castelo':
            ctx.fillStyle = '#800000'; // Vermelho escuro.
            break;
        case 'vila':
            ctx.fillStyle = '#FFD700'; // Amarelo ouro.
            break;
        case 'casa':
            ctx.fillStyle = '#FF8C00'; // Laranja escuro.
            break;
        default:
            ctx.fillStyle = 'white';
            break;
    }
    // Preenche o retângulo com a cor correspondente ao tipo.
    ctx.fillRect(x * tamanho, y * tamanho, tamanho, tamanho);
}
