from lista_encadeada import ListaEncadeada
from lista_duplamente_encadeada import ListaDuplamenteEncadeada
from lista_circular import ListaCircular

def main():
    print("1. TESTANDO LISTA ENCADEADA SIMPLES")
    lista1 = ListaEncadeada()
    lista1.inserir_fim(10)
    lista1.inserir_fim(20)
    lista1.inserir_fim(30)
    print("Lista após inserções:")
    lista1.exibir()
    
    print(f"Buscando o valor 20 (Índice): {lista1.buscar(20)}")
    
    lista1.remover(20)
    print("Lista após remover o 20:")
    lista1.exibir()
    print("\n")


    print("2. TESTANDO LISTA DUPLAMENTE ENCADEADA")
    lista2 = ListaDuplamenteEncadeada()
    lista2.inserir_fim(100)
    lista2.inserir_fim(200)
    lista2.inserir_fim(300)
    print("Exibindo do Início:")
    lista2.exibir_do_inicio()
    print("Exibindo do Fim (Cauda para Cabeça):")
    lista2.exibir_do_fim()
    
    lista2.remover(300)
    print("Exibindo do Início após remover o 300:")
    lista2.exibir_do_inicio()
    print("\n")


    print("3. TESTANDO LISTA CIRCULAR")
    lista3 = ListaCircular()
    lista3.inserir_fim("A")
    lista3.inserir_fim("B")
    lista3.inserir_fim("C")
    print("Lista Circular atual:")
    lista3.exibir()
    
    lista3.percorrer_n_voltas(2)
    
    lista3.remover("A")
    print("Lista Circular após remover o 'A':")
    lista3.exibir()

# Executa o código
if __name__ == "__main__":
    main()