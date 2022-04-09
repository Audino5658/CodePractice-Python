# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inverseChildren(self, node: Optional[TreeNode]):
        
        if node == None:
            return None
        elif node.left == None and node.right == None:
            return 
        else:
            tempNode = node.left
            node.left = node.right
            node.right = tempNode
            self.inverseChildren(node.left)
            self.inverseChildren(node.right)

        '''
        elif node.left == None:
            node.left = node.right
            node.right = None
            self.inverseChildren(node.right)
        elif node.right == None:
            node.right = node.left
            node.left = None
            self.inverseChildren(node.left)
        '''
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.inverseChildren(root)
        return root


    def BFS_Traverse(self, root: Optional[TreeNode]) -> bool:
    
        if root == None:
            return False

        lvl_list = []
        lvl_list.append(self.getChildren(root))

        print(root.val)
        while lvl_list != []:

            nxt_node_list = []
            for broNodes in lvl_list:
                if len(broNodes) == 2:
                    print(broNodes[0].val, broNodes[1].val, end = ' ')
                elif(len(broNodes) == 1):
                    print(broNodes[0].val, end = ' ')

                for node in broNodes: # check 2 nodes' children, and store them for next iteration
                    nxt_node_list.append(self.getChildren(node))

            lvl_list = nxt_node_list
            if lvl_list != []:
                print()
            

    def getChildren(self, parent: Optional[TreeNode])-> list:
        if parent.left != None or parent.right != None:
            if parent.left == None:
                return [parent.right]
            elif parent.right == None:
                return [parent.left]
            else:
                return [parent.left, parent.right]

        return []

def PreorderTraverse(node: TreeNode) -> Optional[TreeNode]:

    if(node ==  None):
        return
    print(node.val)
    PreorderTraverse(node.left)
    PreorderTraverse(node.right)

def ListToTree(InputList: list):

    NodeList = []
    Lchild_i = 1
    Rchild_i = 2
    length = len(InputList)
    for i in range(length):
        if i == 0:
            NodeList.append(TreeNode(InputList[i]))

        if Lchild_i < length:
            NodeList[i].left = TreeNode(InputList[Lchild_i])
            NodeList.append(NodeList[i].left)
            Lchild_i += 2
        if Rchild_i < length:
            NodeList[i].right = TreeNode(InputList[Rchild_i])
            NodeList.append(NodeList[i].right)
            Rchild_i += 2

    return NodeList[0]


def main():

    #input = [4,2,7,1,3,6,9]
    input = [2,3,None,1]
    rootFromInput = ListToTree(input)
    #input = [1,2]
    #input = [2,null,3,null,1]
    '''
    node6 = TreeNode(9)
    node5 = TreeNode(6)
    node2 = TreeNode(7, node5, node6)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    node1 = TreeNode(2, node3, node4)
    root_node = TreeNode(4, node1, node2)
    '''
    node2 = TreeNode(2)
    root_node = TreeNode(1, node2)

    sol = Solution()
    new_root = sol.invertTree(rootFromInput)
    sol.BFS_Traverse(new_root)

    #print(multivalueTest())
    

if __name__ == "__main__":
    main()