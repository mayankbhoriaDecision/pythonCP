

def square(n):
    return n * n;
 
# Recursive function to return sum
# of greatest odd divisor of numbers
# in range [1, n]
def sumX(n):
 
    if (n == 0):
        return 0;
    if (n % 2 == 1):
         
        # Odd n
        return (square(int((n + 1) / 2)) +
                   sum(int(n / 2)));
    else:
         
        # Even n
        return (square(int(n / 2)) +
                   sum(int(n / 2)));
 

T=int(input())

for i in range(T):

    Val=input()

    X=Val.split()


    N=int(X[0])
    M=int(X[1])
    
   
     
    
    print( sumX%M)
