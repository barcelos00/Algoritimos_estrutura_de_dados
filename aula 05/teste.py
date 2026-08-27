#SLICE objetivo de extrair partes da sequencia
#primeiro numero indica onde ira começar a fatia da sequencia 
# ltimo numeor sendo o que indica o valor final da fatia 

print(5//2)
lista = [9,3,8,2,1]
print(lista[0:3]) # ideia de ser como uma bolinha fechada no zero e uma aberta no 3, deixando o valor zero de fora e indo ate o 3 

print(lista[1:4])
print(lista[1:])
print(lista[:])

meio = len(lista) // 2
print(meio)

esq = lista[ : meio] #printando os valores entre o indice 0 e o valor anerior ao que esta presente ao meio da lista (2) printando (9,3)
print(esq)

direita = lista[meio : ] #indo do meio ao final da lista (8,2,1)
print(direita)

#se a lidata fosse PAR entraira certinho um numero par de um lado e outro do outro lado (2 valores de cada lado caso fosse 4 o indice da lista)



