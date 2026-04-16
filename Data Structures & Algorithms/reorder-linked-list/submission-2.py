# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        prev = None
        curr = fast
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        first = head

        while second:
            fn = first.next
            sn = second.next
            first.next = second
            second.next = fn

            first = fn if fn else second
            second = sn

            
        
        