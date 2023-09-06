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







class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        rev=0

        originalval=x

        while(x>0):

            lastdigit=x%10

            rev=rev*10 + lastdigit

            x=x/10


        if(rev==originalval):
            return True
        else:
            return False


        











        
