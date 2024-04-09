def bubble(array):
    n = len(array)
    for j in range(n-1):
        for i in range(0,n-j-1):
            if array[i] > array[i +1]:
                array[i], array[i+1] = array[i,+1], array[i]
        n = n - 1
        print(array)

teste = [5,2,4,6,1,3]

bubble(teste)