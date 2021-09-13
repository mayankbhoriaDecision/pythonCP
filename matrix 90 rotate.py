#Back-end complete function Template for Python 3

class Solution:
    
    #Function to do transpose of matrix.
    def transpose(self,matrix,n):
        R,C=n,n
        for i in range(R): 
            for j in range(i, C): 
                
                #swapping elements at (i,j) and (j,i).
                t = matrix[i][j] 
                matrix[i][j] = matrix[j][i] 
                matrix[j][i] = t 
       
    #after transposing we swap elements of each column (1st with last, 2nd with 
    #second last) one by one for finding left rotation of matrix by 90 degree.
    def reverseColumns(self,matrix,n):
        C=n
        R=n
        for i in range(C): 
            j = 0
            k = C-1
            while j < k: 
                
                #swapping elements in each column.
                t = matrix[j][i] 
                matrix[j][i] = matrix[k][i] 
                matrix[k][i] = t 
                j += 1
                k -= 1
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self,a, n): 
        self.transpose(a,n) 
        self.reverseColumns(a,n) 
