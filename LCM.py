
 
def GCD(A,B):
    
    if(B==0):
        return A 
    else:
        
      return  GCD(B,A%B)
        
        

A=int(input())
B=int(input())

RES=GCD(A,B)

LCM=(A*B)/(RES)

print(LCM)
        
