class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def draw(start,end):

            if start > end:
                return
            node=TreeNode(preorder[start])
            i=start+1

            while i <= end and preorder[i] < preorder[start]:
                i+=1

            node.left=draw(start+1,i-1)
            node.right=draw(i,end)

            return node

        return draw(0,len(preorder)-1)