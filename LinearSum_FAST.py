    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        
        dic={}
        
        
        for i in range(len(nums)):
            
            dic[nums[i]]=i
            
       # print(dic)
    
        i=0
        
        for i in range(len(nums)):
            
            diff=target-nums[i]
            
           # print(diff)
            
            if(diff in dic):
                
                
                
                if(dic[diff]!=i):
                    
                    temp=[]
                    
                    temp.append(i)
                    
                    temp.append(dic[  diff       ])
                    
                    return temp
