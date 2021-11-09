def sub(a,b):
    if(a-b>=0):
        return a-b
    else:
        return b-a

def search(ar,N,x):

    #i nearest

    diff=10000
    minI=0

    for i in range(N):

        if(sub(ar[0][i],x) <diff   and   ar[0][i]<x      ):

            diff=sub(ar[0][i],x)
            minI=i

    diff = 10000
    minJ = 0

    for j in range(N):

        if (sub(ar[j][0] , x) < diff  and ar[j][0]<x           ):


            diff = sub(ar[j][0] , x)
            minJ = j

    if(ar[minJ][minI]==x):

        print(  "(",minJ,",",minI,")" )

    else:
        print("Not Found")


# Driver code
mat = [[10, 20, 30, 40], [15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
search(mat, 4, 29)
