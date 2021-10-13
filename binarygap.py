import math

def onesComplement(n):
 
    
    number_of_bits = (int)(math.floor(math.log(n) /math.log(2))) + 1
 
 
    return ((1 << number_of_bits) - 1) ^ n

def Print_Binary_Number(num):
     
  
    
    return bin(num)


def solution(N):
    # write your code in Python 3.6

    X=onesComplement(N)

    Y=Print_Binary_Number(X)

    Z=Y.split('0b')[1]
    
    
    if('0' not in Z):
        
        return 0
    
    
    

    tmp1=Z.split("0")

    max=0
    
    

    for i in tmp1:

        if('1' in i):

            if(len(list(i))>max):
                
                print(len(list(i)))
                
                max=len(list(i))

    
    if(max!=0):
        return max
    else:
        return 0

    
solution(32)
