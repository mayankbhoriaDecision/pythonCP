class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        word=list(s)
        
        new=[]
        
        
        for i in word:
            
            if(i.isalnum()):
                
                new.append(i.lower())
                
        
        revv=''.join(reversed(new))
        
        
        res=''.join(new)
        
        print(res)
        
        
        if(res==revv):
            return True
        
        else:
            return False
        
