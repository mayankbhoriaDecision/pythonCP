class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        
        
        index1=0
        
        index2=0
        
 
        
        res=[]
        
        
            
            
        while(index1<m and index2<n ):
                
            if(nums1[index1]<=nums2[index2]    ):
                        
                        
                    res.append(nums1[index1])
                        
                    index1+=1
                        
            else:
                        
                    res.append(nums2[index2])
                        
                    index2+=1
                        
                        
                    
        while(index1<m):
            
            
             
                
            
                res.append(nums1[index1])
            
                index1+=1
                
           
            
        while(index2<n):
            
            
            
                
            
                res.append(nums2[index2])
            
                index2+=1
                
            
            
        
                    
        #print(res)
         
        for p in range(len(res)):
            
            nums1[p]=res[p]
            
            
            
            
            
            
