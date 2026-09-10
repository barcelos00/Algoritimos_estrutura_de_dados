
class Vetor:

    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        self.elementos = []

    # 1
    def inserir(self, valor):
        if len(self.elementos) < self.capacidade:
            self.elementos.append(valor)
            print(f"Inserido {valor} -> Vetor atual: {self.elementos}")
        else:
            print(f"Erro: Capacidade máxima ({self.capacidade}) atingida!")


    # 2
    def somar_elementos(self) -> int:
        soma = 0
        for elemento in self.elementos:
            soma += elemento
        return soma

    # 3
    def exibir_maior_valor(self):
        if not self.elementos:
            print("O vetor está vazio.")
            return

        maior = self.elementos[0]
        for elemento in self.elementos[1:]:
            if elemento > maior:
                maior = elemento
        print(f"Maior valor armazenado: {maior}")

    # 4
    def inverter(self):
        inicio = 0
        fim = len(self.elementos) - 1
        while inicio < fim:
            self.elementos[inicio], self.elementos[fim] = (
                self.elementos[fim],
                self.elementos[inicio],
            )
            inicio += 1
            fim -= 1

    def contar_ocorrencias(self, valor) -> int:
        contador = 0
        for elemento in self.elementos:
            if elemento == valor:
                contador += 1
        return contador

    # 6
    def remover_valor(self, valor) -> bool:
        for i in range(len(self.elementos)):
            if self.elementos[i] == valor:
                self.remover(i)
                return True
        return False

    def remover(self, posicao: int):
        if 0 <= posicao < len(self.elementos):
            return self.elementos.pop(posicao)
        return None

    # 7
    def mesclar(self, outro_vetor):
        nova_capacidade = self.capacidade + outro_vetor.capacidade
        novo_vetor = Vetor(nova_capacidade)

        for elemento in self.elementos:
            novo_vetor.inserir(elemento)
        for elemento in outro_vetor.elementos:
            novo_vetor.inserir(elemento)

        return novo_vetor

    # 8
    def ordenar(self):
        n = len(self.elementos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.elementos[j] > self.elementos[j + 1]:
                    self.elementos[j], self.elementos[j + 1] = (
                        self.elementos[j + 1],
                        self.elementos[j],
                    )

    # 9
    def remover_duplicados(self):
        i = 0
        while i < len(self.elementos):
            j = i + 1
            while j < len(self.elementos):
                if self.elementos[j] == self.elementos[i]:
                    self.elementos.pop(j)
                else:
                    j += 1
            i += 1

    # 10
    def redimensionar(self, nova_capacidade: int):
        self.capacidade = nova_capacidade
        if len(self.elementos) > nova_capacidade:
            self.elementos = self.elementos[:nova_capacidade]