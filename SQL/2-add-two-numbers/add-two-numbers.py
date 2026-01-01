class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1. Convert Linked Lists to strings
        z1 = ""
        while l1:
            z1 = str(l1.val) + z1
            l1 = l1.next
            
        z2 = ""
        while l2:
            z2 = str(l2.val) + z2
            l2 = l2.next
            
        # 2. Add the numbers
        total = int(z1) + int(z2)
        
        # 3. Convert total back to a Linked List (reversed)
        # We start by making a 'dummy' head to help build the list
        dummy = ListNode(0)
        current = dummy
        
        # Convert to string and reverse to build nodes in order
        for digit in str(total)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next
            
        return dummy.next