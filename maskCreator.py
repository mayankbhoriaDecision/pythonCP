def subset(arr):

    N=len(arr)
    total_set=1<<N



    for mask in range(total_set):

        tempSet=[]

        for i in range(N):

            f=1<<i

            if(mask&f)!=0:

                tempSet.append(arr[i])

        print(tempSet)
