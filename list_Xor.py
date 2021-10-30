def ConstructList(Q):
 
    # Store cumulative Bitwise XOR
    xor = 0
 
    # Initialize final list to return
    ans = []
 
    # Perform each query
    for i in range(len(Q) - 1, -1, -1):
        if(Q[i][0] == 0):
            ans.append(Q[i][1] ^ xor)
 
        else:
            xor ^= Q[i][1]
 
    # The initial value of 0
    ans.append(xor)
 
    # Sort the list
    ans.sort()
 
    # Return final list
    return ans
 
# Driver Code
 
# Given Queries
Q = [ [0, 6], [0, 3],
      [0, 2], [1, 4],
      [1, 5] ]
 
# Function call
print(ConstructList(Q))
