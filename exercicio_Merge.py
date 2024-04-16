def mergeSort(lista):
    tamanho = len(lista)

    if tamanho == 1:
        return lista

    q = tamanho // 2 #Calcula o ponto central da lista para dividir em duas metades.
    esquerda = mergeSort(lista[:q]) #Chama recursivamente a função mergeSort para ordenar a metade esquerda da lista.
    direita = mergeSort(lista[q:]) #Chama recursivamente a função mergeSort para ordenar a metade direita da lista.

    return merge(esquerda, direita)

def merge(esquerda, direita):
    ordem = []
    
    while esquerda and direita: #Enquanto ambas as listas esquerda e direita não estiverem vazias, o loop continua.
        ordem.append((esquerda if esquerda[0] <= direita[0] else direita).pop(0)) #Compara os primeiros elementos das listas esquerda e direita. O menor entre os dois é removido da sua respectiva lista e adicionado à lista ordem.
    return ordem + esquerda + direita


teste = [10,5,12,1,9]
print(teste)
sorted_list = mergeSort(teste)
print(sorted_list)