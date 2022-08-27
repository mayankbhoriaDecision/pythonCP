

def bubbleSort(Ar):

    n = len(Ar)

    for i in range(n):

        for j in range(n-i-1):

            if (Ar[j] > Ar[j+1]):

                tmp = Ar[j+1]
                Ar[j+1] = Ar[j]
                Ar[j] = tmp

    print(Ar)


Ar = [7, 4, 3, 1, 9, 6, 5]
print(Ar)

bubbleSort(Ar)
