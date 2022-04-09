# https://leetcode.com/problems/insertion-sort-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.nodeList = []

    def createList(self, arrList=[]):
        for i, val in reversed(list(enumerate(arrList))):
            if i == len(arrList)-1:
                self.nodeList.append(ListNode(val)) 
            else:
                next_node = self.nodeList[-1]
                self.nodeList.append(ListNode(val, next_node))
    
    def traverseList(self): 
        node = self.nodeList[-1]  # order is reversed
        while (node.next != None):
            print(node.val)
            node = node.next
        print(node.val)

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        dummy_head = ListNode()    

        while (current_node != None):
            prev_node = dummy_head  # For getting head node
            while( prev_node.next != None and prev_node.next.val < current_node.val):  # Iterating until the current node needs exchange
                prev_node = prev_node.next   
                
            # Exchange the nodes
            tmp_next_node = current_node.next

            current_node.next = prev_node.next
            prev_node.next = current_node

            current_node = tmp_next_node
             
        return dummy_head.next

    def traverseList(self, node: Optional[ListNode]):   
        while (node.next != None):
            print(node.val)
            node= node.next
        print(node.val)

def main():


    head = [4,2,1,3]
    linklist = LinkedList()
    linklist.createList(head)
    #linklist.traverseList()

    
    sol = Solution()
    res = sol.insertionSortList(linklist.nodeList[-1])
    #print(res)
    sol.traverseList(res)

    

if __name__ == "__main__":
    main()