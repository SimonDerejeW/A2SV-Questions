class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_size():
            size = 0
            current = head
            while current:
                size += 1
                current = current.next
            return size
        count = 0
        mid = get_size()//2
        curr = head
        while curr:
            if count == mid:
                return curr
            curr = curr.next
            count+=1
