class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, dummy
        i = n
        while i:
            right = right.next
            i-=1
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next