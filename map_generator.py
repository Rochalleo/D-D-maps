import random
import json

class GeradorDeMapa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.mapa = [["" for _ in range(largura)] for _ in range(altura)]

    def gerar(self):
        self._gerar_biomas()
        self._gerar_rios()
        self._gerar_montanhas()
        self._gerar_estradas()
        self._gerar_estruturas()

    def _gerar_biomas(self):
        biomas = ["floresta", "deserto", "planícies", "pântano", "bosque"]
        for y in range(self.altura):
            for x in range(self.largura):
                self.mapa[y][x] = random.choice(biomas)

    def _gerar_rios(self):
        num_rios = random.randint(1, 9)
        for _ in range(num_rios):
            x, y = random.randint(0, self.largura - 3), random.randint(0, self.altura - 3)
            comprimento = random.randint(5, 100)
            direcao = random.choice([(0, 1), (1, 0, 0, -1), (-1, 0, 1, -1), (-1, 1, 0, -1, 1, 0)])

            for _ in range(comprimento):
                if 0 <= x < self.largura and 0 <= y < self.altura:
                    self.mapa[y][x] = "rio"
                    x += direcao[0]
                    y += direcao[1]

    def _gerar_montanhas(self):
        num_montanhas = random.randint(5, 15)
        for _ in range(num_montanhas):
            x, y = random.randint(0, self.largura - 5), random.randint(0, self.altura - 5)
            self.mapa[y][x] = "montanha"
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < self.largura and 0 <= y + dy < self.altura:
                        if self.mapa[y + dy][x + dx] != "montanha":
                            self.mapa[y + dy][x + dx] = "colina"

    def _gerar_estradas(self):
        num_estradas = random.randint(2, 25)
        for _ in range(num_estradas):
            x, y = random.randint(0, self.largura - 1), random.randint(0, self.altura - 1)
            comprimento = random.randint(10, 20)
            direcao = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1)])

            for _ in range(comprimento):
                if 0 <= x < self.largura and 0 <= y < self.altura:
                    tipo = "estrada de terra" if random.random() < 0.7 else "estrada de calcamento"
                    self.mapa[y][x] = tipo
                    x += direcao[0]
                    y += direcao[1]

    def _gerar_estruturas(self):
        estruturas = {"castelo": 1, "vila": 3, "casa": 10}

        for estrutura, quantidade in estruturas.items():
            for _ in range(quantidade):
                x, y = random.randint(0, self.largura - 5), random.randint(0, self.altura - 5)
                if self.mapa[y][x] not in ["rio", "montanha", "colina"]:
                    self.mapa[y][x] = estrutura

    def expandir_mapa(self):
        novo_mapa = []
        for linha in self.mapa:
            for _ in range(9):  # Cada linha vira 9 linhas
                nova_linha = []
                for celula in linha:
                    nova_linha.extend([celula] * 9)  # Cada célula vira 9 células
                novo_mapa.append(nova_linha)
        self.mapa = novo_mapa
        self.largura *= 9
        self.altura *= 9

    def salvar_para_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(self.mapa, arquivo)

if __name__ == "__main__":
    largura = 35   # Reduzido para gerar mapas mais detalhados sem consumir muita memória
    altura = 35 
    gerador = GeradorDeMapa(largura, altura)
    gerador.gerar()
    gerador.expandir_mapa()
    gerador.salvar_para_arquivo("mapa_realista.json")
    print("Mapa gerado e salvo em mapa_realista.json.")
