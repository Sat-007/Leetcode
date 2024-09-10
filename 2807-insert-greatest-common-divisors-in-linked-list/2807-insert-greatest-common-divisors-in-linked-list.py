# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Head =     18 -> 6 -> 10 -> 3 
        output 18 -> 6 -> 6 -> 2 -> 10 -> 1 -> 3
                    new       new      new
                    
                    the new nodes are the GCD of the 1st two nodes, then next two and so on ....
                    GCD
        """
        
        def gcd(x,y):
            while y != 0:
                x, y = y, x % y
            return x
        curr = head
        prev = None
        n = head.next
        
        while head is None and head.next is None:
            return head
        
        
        while n is not None:
            val1 = gcd(curr.val, n.val)
            temp = ListNode(val1)
            prev = curr
            curr = n 
            n = n.next
            temp.next = curr
            prev.next = temp 
            
        return head
                