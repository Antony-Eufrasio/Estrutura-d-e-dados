def selection(item):
    n = len(item)
    for i in range(n-1): #Começa um loop que itera sobre os elementos da lista até o penúltimo elemento.
        valorMin = i #Define o índice do elemento atual como o índice do menor valor

        for j in range(i+1, n): #Começa um segundo loop que itera sobre os elementos da lista a partir do próximo elemento após o elemento atual até o último elemento.
            if item[j] < item[valorMin]: # Verifica se o elemento atual é menor que o elemento atualmente considerado como o menor.
                valorMin = j #Se o elemento atual for menor que o atualmente considerado como o menor, atualizamos o índice do menor valor para o índice do elemento atual.

        if valorMin != i: #Verifica se houve uma mudança no índice do menor valor em relação ao índice do elemento atual.
            temp = item[i] #Se houve uma mudança no índice do menor valor, trocamos os elementos de posição na lista para colocar o menor elemento na posição correta.
            item[i] = item[valorMin]
            item[valorMin] = temp
    print(item)

elementos = [21,34,54,2,15]

selection(elementos) 

