import array as arr
class Solution:
    def isPalindrome(self, number):
        numString = str(number)
        reverseNumber = ""
        newArr = []
        i = 0
        length = len(numString)
        while(i<length):
            newArr.append(numString[i])
            i = i + 1
        reversedArr = reversed(newArr)
        finalArr = list(reversedArr)
        
        # Final Reversed Array
        # print(finalArr)
        for num in finalArr:
            reverseNumber = reverseNumber + num
        print(number)
        print(reverseNumber)
        if (str(reverseNumber) == str(number)):
            print("Number is Palindrome")
            return True
        else:
            print("Number is not Palindrome")
            return False
       
