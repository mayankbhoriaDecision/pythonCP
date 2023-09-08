
def Count_Trailing_zeroes_in_factorial(N):
    
    res=0
    
    i=5
    
    while(i<=N):
        
        res=res+N//i 
      
        i=i*5
        
    return res 

Num=int(input())


print(Count_Trailing_zeroes_in_factorial(Num))
