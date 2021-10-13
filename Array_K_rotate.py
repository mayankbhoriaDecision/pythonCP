def rotate_one(A):
    
    N=len(A)
    
    tmp=[]
    
    tmp.append(A[N-1])
    
    A.remove(A[N-1])
    
    tmp+=A
    
    return tmp
    
    
