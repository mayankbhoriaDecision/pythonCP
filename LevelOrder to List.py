# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        
        size=  self.height(root)
        
        
        global tmp
        
        ans=[]
        
        
        for X in range(1,size+1):
            
            tmp=[]
            
            self.printCurrentLevel(root,X)
            
            #print(tmp)
            
            ans.append(tmp)
        
        
        
        return ans
        
        
    def printCurrentLevel(self,root , level):
        
        global tmp
        
        
        if root is None:
            return
        if level == 1:
            
            tmp.append(root.val)
            
        elif level > 1 :
            self.printCurrentLevel(root.left , level-1)
            self.printCurrentLevel(root.right , level-1)        
        
        
        
        
        
        
    
    def height(self,root):
        
        if root==None:
            
            return 0
        
        
        
        
        
        L=self.height(root.left)
        
        R=self.height(root.right)
        
        if(L>R):
            return L+1
        
        else:
            
            return R+1
        
        
        
        
        
        
        
