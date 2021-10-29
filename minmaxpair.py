




def FindIndex(a,N,X):


    for i in range(N):

        for j in range(N):

            if(a[i][j]==X):

                temp=[]
                temp.append(i)
                temp.append(j)

                return  temp

    return -1






















def MinMaxPair(a):


    N=len(a)


    dp=[]

    for i in range(N):

        tmp=[]

        for j in range(N):

            tmp.append(0)

        dp.append(tmp)








    calc=[]


    for i in range(N):
        for j in range(N):



            dp[i][j]=a[i]^a[j]

            if(dp[i][j]!=0):

                calc.append(dp[i][j])




    calc.sort()


    max_index=[]

    max_sum=0

    mcalc=calc

    mcalc.reverse()


    target=N/2


   # print(mcalc)

    for val in mcalc:

        if(target>0):

            temp=FindIndex(dp,N,val)

            if(temp!=-1):

                if(  temp[0] not in max_index and temp[1] not in max_index     ):

                    max_index.append(temp[0])
                    max_index.append(temp[1])

                    max_sum+=val

                    target-=1






#minimum

    min_sum=0

    min_index=[]

    target=N/2


    calc.reverse()

   # print(calc)

    for val in calc:

        if(target>0):

            temp=FindIndex(dp,N,val)

            if(temp!=-1):

                if(  temp[0] not in min_index and temp[1] not in min_index     ):

                    min_index.append(temp[0])
                    min_index.append(temp[1])

                    min_sum+=val

                    target-=1


    print(str(min_sum)+" "+str(max_sum) )






































ar=[1,2,3,4]

MinMaxPair(ar)








