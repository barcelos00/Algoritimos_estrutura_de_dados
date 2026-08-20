import time
from bubble_sort import bubble_sort, bubble_sort_otimizado
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from utilitarios import ler_lista_do_usuario, exibir_resultado
from utilitarios import gerar_lista_aleatoria, gerar_lista_quase_ordenada

def exibir_menu():
    print("")
    print("1. Bubble Sort (versão básica)")
    print("2. Bubble Sort (versão otimizada)")
    print("3. Selection Sort")
    print("4. Insertion Sort")
    print("5. Comparação rápida (Bubble x Selection)")
    print("6. Comparação de desempenho (os três algoritmos)")
    print("0. Sair")

def executar_comparacao_rapida():
    lista = ler_lista_do_usuario()
    copia_bubble = list(lista)
    copia_selection = list(lista)
    print("Bubble Sort otimizado:")
    resultado_bubble = bubble_sort_otimizado(copia_bubble)
    print("Selection Sort:")
    resultado_selection = selection_sort(copia_selection)
    print("Resultado Bubble Sort otimizado: " + str(resultado_bubble))
    print("Resultado Selection Sort: " + str(resultado_selection))

def executar_comparacao_desempenho():
    tamanho = int(input("Digite o tamanho da lista para o teste: "))
    lista_aleatoria = gerar_lista_aleatoria(tamanho)
    lista_quase_ordenada = gerar_lista_quase_ordenada(lista_aleatoria)
    
    algoritmos = [
        ("Bubble Sort otimizado", bubble_sort_otimizado),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
    ]
    
    print("")
    print("Resultados com lista aleatória:")
    for nome, funcao in algoritmos:
        copia = list(lista_aleatoria)
        inicio = time.perf_counter()
        funcao(copia)
        fim = time.perf_counter()
        tempo = round(fim - inicio, 4)
        print(nome + " - tempo: " + str(tempo) + " s")
        
    print("")
    print("Resultados com lista quase ordenada:")
    for nome, funcao in algoritmos:
        copia = list(lista_quase_ordenada)
        inicio = time.perf_counter()
        funcao(copia)
        fim = time.perf_counter()
        tempo = round(fim - inicio, 4)
        print(nome + " - tempo: " + str(tempo) + " s")

def main():
    opcao = -1
    while opcao != 0:
        exibir_menu()
        entrada = input("Escolha uma opção: ")
        try:
            opcao = int(entrada)
        except ValueError:
            print("Opcao invalida.")
            continue
            
        if opcao == 1:
            lista = ler_lista_do_usuario()
            resultado = bubble_sort(list(lista))
            exibir_resultado("Bubble Sort básico", resultado)
        elif opcao == 2:
            lista = ler_lista_do_usuario()
            resultado = bubble_sort_otimizado(list(lista))
            exibir_resultado("Bubble Sort otimizado", resultado)
        elif opcao == 3:
            lista = ler_lista_do_usuario()
            resultado = selection_sort(list(lista))
            exibir_resultado("Selection Sort", resultado)
        elif opcao == 4:
            lista = ler_lista_do_usuario()
            resultado = insertion_sort(list(lista))
            exibir_resultado("Insertion Sort", resultado)
        elif opcao == 5:
            executar_comparacao_rapida()
        elif opcao == 6:
            executar_comparacao_desempenho()
        elif opcao == 0:
            print("Encerrando o programa.")
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()