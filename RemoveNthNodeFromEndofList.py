    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_size():
            size = 0
            current = head
            while current:
                size += 1
                current = current.next
            return size
        index = get_size()-n
        if index == 0:
            head = head.next
        count = 1
        curr = head
        while curr:
            if count == index:
                curr.next = curr.next.next
            curr = curr.next
            count+=1
        return head
