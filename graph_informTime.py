from collections import defaultdict



class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        def dfs(node,curTime):

            nonlocal ans

            if node not in graph:

                ans=max(ans,curTime)

            for child in graph[node]:
                dfs(child,curTime+informTime[node])

            
        graph=defaultdict(list)
        
        
        for x in range(len(manager)):
            
            graph[manager[x]].append(x)

      

        ans=0

        dfs(headID,0)

        return ans
