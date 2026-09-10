from vetor import Vetor

print(" 1 ")
v1 = Vetor(6)
v1.inserir(5)
v1.inserir(10)
v1.inserir(15)

print("2")
print(f"Soma de todos os elementos: {v1.somar_elementos()}")

print("3")
v1.exibir_maior_valor()

print("4")
v1.inverter()
print(f"Vetor após inverter: {v1.elementos}")

print("5")
v1.inserir(10)  
print(f"Ocorrências do número 10: {v1.contar_ocorrencias(10)}")

print("6")
v1.remover_valor(10)
print(f"Após remover primeira ocorrência do 10: {v1.elementos}")

print("7")
v2 = Vetor(3)
v2.inserir(20)
v2.inserir(30)
v3 = v1.mesclar(v2)
print(f"Novo vetor mesclado: {v3.elementos}")

print("8")
v3.ordenar()
print(f"Vetor ordenado: {v3.elementos}")

print(" 9")
v3.inserir(15)  
print(f"Antes de remover duplicados: {v3.elementos}")
v3.remover_duplicados()
print(f"Após remover duplicados: {v3.elementos}")

print("10")
v3.redimensionar(3)
print(
    f"Elementos após redimensionar para 3: {v3.elementos} (Capacidade atual: {v3.capacidade})"
)