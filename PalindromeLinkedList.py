    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        elem1 = []
        elem2 = []
        
        curr = head
        while curr != None:
            elem1.append(curr.val)
            curr = curr.next 
        
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        
        while prev:
            elem2.append(prev.val)
            prev = prev.next
        if elem1 == elem2:
            return True 
        else:
            return False
