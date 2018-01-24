class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if(inorder):
            ind=inorder.index(preorder[0])
            root=TreeNode(preorder.pop(0))
            root.left=self.buildTree(preorder,inorder[:ind])
            root.right=self.buildTree(preorder,inorder[ind+1:])
            return root
sol=Solution()
# print(24//7)
val=sol.buildTree([1,2],[1,2])