class Solution:
    def getSecondLargest(self, arr):
        
        large = None
        sec = None
        
        for i in arr:
            if large is None or i>large:
                sec=large
                large=i
            elif (sec is None and i== large )or (i>sec  and i < large):
                sec=i
        
        if sec==large:
            return -1
        else :
            return sec
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna