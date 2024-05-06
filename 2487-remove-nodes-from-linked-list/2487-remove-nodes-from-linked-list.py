# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev, cur = None, head
            while cur:
                temp = cur.next
                cur.next = prev 
                prev,cur = cur, temp
                
            return prev
            
        head = reverse(head)
        
        cur = head
        max_cur = cur.val
        while cur.next:
            if cur.next.val < max_cur:
                cur.next = cur.next.next
            else:
                max_cur = cur.next.val
                cur = cur.next
        
        return reverse(head)
                
        