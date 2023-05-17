class Solution:
    def removeElement(self, nums, val):
        i = 0
        for number in nums:
            if (number != val):
                nums[i] = number
                i += 1

        return i
    
        