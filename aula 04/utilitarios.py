import random

def ler_lista_do_usuario():
    while True:
        entrada = input("Digite os números separados por espaço: ")
        partes = entrada.split()
        try:
            lista = [int(valor) for valor in partes]
            return lista
        except ValueError:
            print("Entrada inválida. Use apenas inteiros.")

def exibir_resultado(nome_algoritmo, lista_ordenada):
    print("Algoritmo utilizado: " + nome_algoritmo)
    print("Lista ordenada: " + str(lista_ordenada))

def gerar_lista_aleatoria(tamanho):
    lista = [random.randint(0, 9999) for _ in range(tamanho)]
    return lista

def gerar_lista_quase_ordenada(lista):
    quase = sorted(lista)
    if len(quase) > 1:
        meio = len(quase) // 2
        ultimo = len(quase) - 1
        quase[meio], quase[ultimo] = quase[ultimo], quase[meio]
    return quase