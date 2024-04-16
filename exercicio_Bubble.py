def bubble(array):
    for j in range(0, len(array)-1): # Este for é utilizado para que o 
        programa sempre percorra a lista, excluindo o ultimo valor, já que ele não teria nenhum outro numero para se comparar.
        for i in range(0, len(array)-1):
            if array[i]>array[i+1]: # If sendo utilizado para comparar o valor do indice com o proximo.
                array[i], array[i+1] = array[i+1], array[i] # Caso a condição do if seja atendida, os valores irão trocar de lugar
 
teste = [21,34,54,2,15]
bubble(teste)

print(teste)