from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        dic = defaultdict(int)

        
        
        
        for i in nums:
            
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
                
        res=[]
        
        count=1
        
        for w in sorted(dic, key=dic.get, reverse=True):
            
            if(count<=k):
                
                res.append(w)
                
            count+=1
                
        
        return res
            
            
     
        
