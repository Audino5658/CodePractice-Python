#https://leetcode.com/problems/reverse-nodes-in-k-group/

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

        # Order is reversed
        self.nodeList.reverse()
    
    def traverseList(self): 
        node = self.nodeList[0]  
        while (node.next != None):
            print(node.val)
            node = node.next
        print(node.val)


    def reverseList(self, head):
        if (head == None or head.next == None):
            return head

        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return rest


    def replaceRevList(self):
        node = self.nodeList[0]  
        node = self.reverseList(node)
        self.nodeList.clear()
        self.nodeList.append(node)


    def getHead(self):
        return self.nodeList[0]


class Solution:
    def reverseList(self, head):
        if (head == None or head.next == None):
            return head

        rest = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return rest

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Get linkedList length
        lstLen = 0
        node = head
        while node != None:
            lstLen += 1
            node = node.next 

        # m = lstLen/k                  #    m: total count of k-group 
        rest = lstLen - lstLen%k      # rest: The rest node index
        group_head_list = []

        node = head
        restNode_head = None
        for i in range(lstLen):
            if i < rest:
                # Cpnfirm whether entering rest part.
                if i % k == 0 :
                    group_head_list.append(node)
                # When 1 k-group end. Make next node become null and store next node.     
                if i % k == k-1 : 
                    nextnode = node.next
                    node.next = None
                    node = nextnode
                else:
                    node = node.next
            else:
                restNode_head = node

        revGrp_head_list = []
        for node in group_head_list:
            rev_head = self.reverseList(node)
            revGrp_head_list.append(rev_head)
            
        
        for i, node in enumerate(revGrp_head_list):
            if i < len(revGrp_head_list)-1: 
                while (node.next != None):
                    node = node.next
                node.next = revGrp_head_list[i+1]
            else:
                while (node.next != None):
                    node = node.next
                node.next = restNode_head                                           

        return revGrp_head_list[0]

        '''  print out   
        new_head = revGrp_head_list[0]
        while (new_head.next != None):
            print(new_head.val)
            new_head = new_head.next
        print(new_head.val)
        '''   


def main():
    
    input = [1,2,3,4,5]
    linklst = LinkedList()
    linklst.createList(input)
    #linklst.replaceRevList()
    #linklst.traverseList()

    sol = Solution()
    sol.reverseKGroup(linklst.getHead(), 2)


if __name__ == "__main__":
    main()