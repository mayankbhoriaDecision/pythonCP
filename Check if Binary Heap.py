# Python3 program to check whether a
# given array represents a max-heap or not
 
# Returns true if arr[i..n-1]
# represents a max-heap
def isHeap(arr, i, n):
     
    # If (2 * i) + 1 >= n, then leaf node, so return true
    if i >= int((n - 1) / 2):
        return True
     
    # If an internal node and is greater
    # than its children, and same is
    # recursively true for the children
    if(arr[i] >= arr[2 * i + 1] and
       arr[i] >= arr[2 * i + 2] and
       isHeap(arr, 2 * i + 1, n) and
       isHeap(arr, 2 * i + 2, n)):
        return True
     
    return False
 
# Driver Code
if __name__ == '__main__':
    arr = [90, 15, 10, 7, 12, 2, 7, 3]
    n = len(arr) - 1
 
    if isHeap(arr, 0, n):
        print("Yes")
    else:
        print("No")
 
# This code is contributed by PranchalK
