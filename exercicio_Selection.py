def selection(item):
    n = len(item)
    for i in range(n-1):
        valorMin = i

        for j in range(i+1, n):
            if item[j] < item[valorMin]:
                valorMin = j

        if valorMin != i:
            temp = item[i]
            item[i] = item[valorMin]
            item[valorMin] = temp
    print(item)

elementos = [21,34,54,2,15]

selection(elementos) 

