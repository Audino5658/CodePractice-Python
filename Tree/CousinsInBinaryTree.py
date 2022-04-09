# https://leetcode.com/problems/cousins-in-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



def traverse(node: TreeNode):

    if(node ==  None):
        print(None)
        return
    print(node.val)
    traverse(node.left)
    traverse(node.right)



class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    
        if root == None:
            return False

        lvl_list = []
        lvl_list.append(self.getChildren(root))

        while lvl_list != []:

            found = 0
            nxt_node_list = []
            for broNodes in lvl_list:
                
                if len(broNodes) == 1 :   # 1 of node is none
                    if x == broNodes[0].val or y == broNodes[0].val:
                        found += 1
                elif len(broNodes) == 2:  # 2 nodes have values
                    if [x,y] in [broNodes[0].val, broNodes[1].val]:
                        return False
                    elif x in [broNodes[0].val, broNodes[1].val] or y in [broNodes[0].val, broNodes[1].val]:
                        found += 1

                if found >= 2 :
                    return True

                for node in broNodes: # check 2 nodes' children, and store them for next iteration
                    nxt_node_list.append(self.getChildren(node))

            lvl_list = nxt_node_list
        return False

    def getChildren(self, parent: Optional[TreeNode])-> list:
        if parent.left != None or parent.right != None:
            if parent.left == None:
                return [parent.right]
            elif parent.right == None:
                return [parent.left]
            else:
                return [parent.left, parent.right]

        return []


def multivalueTest():
    res = all ( x in [1,2,3,4] for x in [6, 4])
    return res


def main():

    #root = [1,2,3,null,4,null,5], x = 5, y = 4
    #root = [1,2,3,4]
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node2 = TreeNode(2, None, node4)
    node3 = TreeNode(2, None, node5)
    root_node = TreeNode(1, node2, node3)

    #traverse(root_node)
    x = 5
    y = 4
    sol = Solution()
    res = sol.isCousins(root_node, x, y)
    print(res)

    #print(multivalueTest())
    

if __name__ == "__main__":
    main()
        