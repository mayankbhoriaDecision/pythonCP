#code
import heapq


from heapq import heappop, heappush, heapify
  
  
T=int(input())

for i in range(T):
    
    r=input()
    
    r2=r.split()
    
    N=int(r2[0])
    
    K=int(r2[1])
    
    b=input()
    
    terms=b.split()
    
    heap = []
    
    heapify(heap)
    
    for x in terms:
        
        heappush(heap, -1 * int(x))
        
        
    for j in range(K-1):
        
        heapq.heappop(heap )
    
    print(str(-1 * heap[0]))
