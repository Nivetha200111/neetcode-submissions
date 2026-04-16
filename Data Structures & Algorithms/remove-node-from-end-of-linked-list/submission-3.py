class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        l = 0
        while curr:
            l += 1
            curr = curr.next
        if l == n:
            return head.next
        curr = head
        i = 0
        while curr:
            if l - i - 1 == n:
                curr.next = curr.next.next
                break
            curr = curr.next
            i+=1
        return head