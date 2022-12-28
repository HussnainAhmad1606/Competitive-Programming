class Solution:
    def plusOne(self, array):
        digits = ""
        for num in array:
            digits += str(num)
        digits = int(digits) + 1    
        finalArr = []
        for digit in str(digits):
            finalArr.append(int(digit))
            
        return finalArr