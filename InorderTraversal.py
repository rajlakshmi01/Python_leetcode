class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(root:[TreeNode]):
        inord = []
        def inorder(curr=root):
            nonlocal inord
            if curr:
                inorder(curr.left)
                inord.append(curr.val)
                inorder(curr.right)
            return
        inorder()
        return inord
    
a=TreeNode([1,null,2,3])
print(Solution.inorderTraversal(a))