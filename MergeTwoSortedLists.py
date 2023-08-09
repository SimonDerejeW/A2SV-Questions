    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        curr = list1
        while curr:
            lis.append(curr.val)
            curr = curr.next
        curr = list2
        while curr:
            lis.append(curr.val)
            curr = curr.next
        lis.sort()

        if len(lis)!=0:
            new_head = ListNode(lis[0])
            curr = new_head
            for i in lis[1:]:
                newnode = ListNode(i)
                curr.next = newnode
                curr = curr.next
            
            return new_head
        else:
            return None
            
