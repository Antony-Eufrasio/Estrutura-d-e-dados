def quick(numeros):
    tamanho = len(numeros)
    if tamanho <= 1:
        return numeros
    
    pivot = numeros.pop() #Remove e atribui o último elemento da lista como pivô. O pivô é um elemento chave usado para particionar a lista em duas partes: uma com elementos menores que o pivô e outra com elementos maiores que o pivô.
    maior, menor = [], [] # Inicializa duas listas vazias, uma para armazenar os elementos maiores que o pivô e outra para armazenar os elementos menores que o pivô.
    for number in numeros:
        if number > pivot: # Se o elemento for maior que o pivô, ele é adicionado à lista maior.
            maior.append(number) 
        else: #Se o elemento não for maior que o pivô ele é adicionado à lista menor.
            menor.append(number)
    return quick(menor) + [pivot] + quick(maior) #Chama recursivamente a função quick para as sublistas menores e maiores, e concatena essas sublistas com o pivô no meio.
teste = [10,5,12,1,9,7]
print(quick(teste))
