 def sumOfLeafNodes(root):
    #Your code her
    
    
    global ans
    
    ans=0
    
    getLeafs(root)
    
    return ans
    
    
    
def getLeafs(root):
    
    global ans
    
    if root==None:
        return 
    
    if root.left is None and root.right is None:
        
        ans+=root.data
        
        
        
    getLeafs(root.left)
    getLeafs(root.right)
    
    
