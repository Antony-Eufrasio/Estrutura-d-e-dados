teste = [5,2,4,6,1,3]

def insertion(add):
    n = len(add)
    for i in range(1,n):
        key = add[i]
        j = i-1

        while j >= 0 and add[j] > key:
            add[j+1] = add[j]
            j = j-1
        add[j+1] = key

        print(add)


insertion(teste)

