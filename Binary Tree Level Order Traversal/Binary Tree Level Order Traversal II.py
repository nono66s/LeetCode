# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer=[]
        self.traversal(root,1,answer)
        answer.reverse()
        return answer
    
    def traversal(self,data,depth,answer):
        if data==None:
            return
        if depth>len(answer):
            answer.append([data.val])
        else:
            answer[depth-1].extend([data.val])
        self.traversal(data.left,depth+1,answer)
        self.traversal(data.right,depth+1,answer)
            
            
            