# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MySolution(object):

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        res_node_lst = ListNode()
        carry = 0
        n = None   # The head of the Linked list  

        count = 0
        while l1 != None and l2 != None:
            
            x = 0
            if l1 != None:
                x = l1.val
                l1 = l1.next
                
            y = 0
            if l2 != None:
                y = l2.val 
                l2 = l2.next    
                
            sum = x + y + carry
            carry = int( sum/10 )
            
            if (count == 0):
                n = ListNode( val = sum % 10 )
                res_node_lst = n
                count+=1
            else:
                n.next = ListNode( val = sum % 10 )
                n = n.next

            
        
        if (carry == 1):
            n.next = ListNode(val = 1)
            n =  n.next

        n.next = None
        return res_node_lst



    # Pseudocode
    '''
    Initialize current node to dummy head of the returning list.
    Initialize carry to 0.
    Initialize p and q to head of l1 and l2 res_nodepectively.

    Loop through lists l1 and l2 until you reach both ends.
        Set x to node p's value. If p has reached the end of l1, set to 0.
        Set y to node q's value. If q has reached the end of l2, set to 0.
        Set sum = x + y + carry.
        Update carry = sum / 10.
        Create a new node with the digit value of (sum mod 10) and set it to current node's next, then advance current node to next.
        Advance both p and q.

    Check if carry = 1, if so append a new node with digit 11 to the returning list.
    Return dummy head's next node.
    '''





class SampleSolution(object):

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        index = 0
        res_nodeult = ListNode()
        while l1 is not None or l2 is not None or carry >  0:
            sumval = carry
            if l1 is not None:
                sumval += l1.val
                l1 = l1.next
            if l2 is not None:
                sumval += l2.val
                l2 = l2.next
            carry = sumval // 10
            sumval = sumval % 10
            if index == 0:
                n = res_nodeult
                n.val = sumval
                index += 1
            else:
                n.next = ListNode(sumval)
                n = n.next
        return res_nodeult

def main():

    #linked list 1
    nA1 = ListNode(2)
    nA2 = ListNode(4)
    nA1.next =nA2
    nA3 = ListNode(3)
    nA2.next =nA3

    #linked list 2
    nB1 = ListNode(5)
    nB2 = ListNode(6)
    nB1.next =nB2
    nB3 = ListNode(4)
    nB2.next =nB3


    #sol = SampleSolution()
    #sol.addTwoNumbers(nA1, nB1)

    sol2 = MySolution()
    sol2.addTwoNumbers(nA1, nB1)

if __name__ == '__main__':
    main()


 
  
