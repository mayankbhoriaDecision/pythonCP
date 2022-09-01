#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    # Write your code here
     
    
    LR_sum=0
    
    for i in range(0,n):
        
        for j in range(0,n):
        
            if(i==j):
                
                LR_sum+=arr[i][j]
                
    RL_sum=0
    
    for p in range(n-1,-1,-1):
        
        for q in range(0,n):
            
            if(p+q==n-1):
                RL_sum+=arr[p][q]
                
   # print(LR_sum)
   # print(RL_sum)
    
    
    diff=RL_sum-LR_sum
    
    if(diff<0):
        diff*=-1
    
    return diff
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
