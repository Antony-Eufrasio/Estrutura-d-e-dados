teste = [5,2,4,6,1,3]

def insertion(add):
    n = len(add)
    for i in range(1,n): #Começa um loop que itera sobre os elementos da lista a partir do segundo elemento até o último.
        key = add[i] #Armazena o valor do elemento atual (add[i]) em uma variável chamada key.
        j = i-1 

        while j >= 0 and add[j] > key: #inicia um loop enquanto j é maior ou igual a zero e o elemento na posição j é maior que a key.
            add[j+1] = add[j] #Move o elemento na posição j para a direita, criando espaço para inserir a key.
            j = j-1
        add[j+1] = key #Insere a key na posição correta no array ordenado.

        print(add)


insertion(teste)

