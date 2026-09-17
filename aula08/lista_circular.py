class NoCircular:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaCircular:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def inserir_fim(self, valor):
        novo = NoCircular(valor)
        if self.cabeca is None:
            self.cabeca = novo
            novo.proximo = novo
        else:
            atual = self.cabeca
            while atual.proximo is not self.cabeca:
                atual = atual.proximo
            atual.proximo = novo
            novo.proximo = self.cabeca
        self.tamanho += 1

    def exibir(self):
        if self.cabeca is None:
            print([])
            return
        
        valores = []
        atual = self.cabeca
        
        while True:
            valores.append(atual.valor)
            atual = atual.proximo
            if atual is self.cabeca:
                break
                
        print(valores)

    def percorrer_n_voltas(self, voltas):
        if self.cabeca is None:
            return
            
        total = self.tamanho * voltas
        atual = self.cabeca
        
        for _ in range(total):
            print(atual.valor)
            atual = atual.proximo

    def remover(self, valor):
        if self.cabeca is None:
            return False
            
        anterior = None
        atual = self.cabeca
        
        while True:
            if atual.valor == valor:
                # Se o elemento a ser removido for a cabeça da lista
                if atual is self.cabeca:
                    # Se for o único elemento na lista
                    if atual.proximo is self.cabeca:
                        self.cabeca = None
                    else:
                        # Precisamos encontrar o último elemento para atualizar o ponteiro
                        ultimo = self.cabeca
                        while ultimo.proximo is not self.cabeca:
                            ultimo = ultimo.proximo
                        
                        self.cabeca = atual.proximo
                        ultimo.proximo = self.cabeca
                else:
                    # Se for um elemento no meio ou no fim
                    anterior.proximo = atual.proximo
                    
                self.tamanho -= 1
                return True
            
            anterior = atual
            atual = atual.proximo
            
            # Se demos a volta completa e não encontramos
            if atual is self.cabeca:
                break
                
        return False