

def findMissingNumber(ar, N):

    Sum_of_ar = sum(ar)

    Sum_of_N_vals = (N*(N+1))/2

    Missing_Val = Sum_of_N_vals-Sum_of_ar

    print(Missing_Val)


arr = [1, 2, 4, 6, 3, 7, 8]
N = 8


findMissingNumber(arr, N)
