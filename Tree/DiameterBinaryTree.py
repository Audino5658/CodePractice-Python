# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self) -> None:
        self.max_d = 0

    def traverse(self, node: TreeNode, length: int, max_length = 0):
        length += 1
        if(node ==  None):
            #print(str(length) + ' ' + str(node.val))
            length -=1
            return max(length-1, max_length)
        else:
            max_length = self.traverse(node.left, length, max_length)
            max_length = self.traverse(node.right, length, max_length)

        return max_length

    def diameterOfBinaryTree_bad(self, root: Optional[TreeNode]) -> int:

        length_L = 0
        if root.left!= None:
            length_L +=1
            length_L += self.traverse(root.left, 0) 
            #print(self.traverse(root.left, 0))

        length_R = 0
        if root.right!= None:
            length_R +=1
            length_R += self.traverse(root.right, 0) 
            #print(self.traverse(root.right, 0))

        return length_L + length_R

    
    def DFSutil(self, node: Optional[TreeNode]) -> int:
        if node == None:
            return 0

        l_d = self.DFSutil(node.left)
        r_d= self.DFSutil(node.right)

        self.max_d = max(self.max_d, l_d+r_d)
        #print(str(node.val) + ": "+ str(max_d))

        return max(l_d, r_d) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.DFSutil(root)
        
        return self.max_d



def traverse(node: TreeNode):

    if(node ==  None):
        return
    print(node.val)
    traverse(node.left)
    traverse(node.right)


def main():

    #input = [3,1,null,null,2]
     #input = [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
    '''
    input = [1,2,3,4,5]
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    root_node = TreeNode(1, node2, node3)
    '''
    #node5 = TreeNode(2)
    #node2 = TreeNode(1, None, node5)
    #root_node = TreeNode(3, node2, None)
    #traverse(root_node)

    node2 = TreeNode(2)
    root_node = TreeNode(1, node2)

    sol = Solution()
    res = sol.diameterOfBinaryTree(root_node)
    print(res)

    #print(multivalueTest())
    

if __name__ == "__main__":
    main()