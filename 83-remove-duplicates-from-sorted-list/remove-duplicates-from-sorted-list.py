class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                 # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
            
        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna