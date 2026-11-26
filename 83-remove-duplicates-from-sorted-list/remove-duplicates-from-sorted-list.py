class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head
        next_node = None

        while current is not None and current.next is not None:
            next_node = current.next
            if current.val == next_node.val:
                 # Skip the duplicate node
                current.next = next_node.next
            else:
                # Move to the next node
                current = next_node
            
        return head
        """
        Current	Next	Action
           1	 1	  Skip duplicate
           1	 2	  Move forward
           2	 3	  Move forward
           3	 3	  Skip duplicate"""

        # current = head

        # while current is not None and current.next is not None:
        #     if current.val == current.next.val:
        #         # Skip the duplicate node
        #         current.next = current.next.next

        #     else:
        #         # Move to the next node
        #         current = current.next

        # return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna