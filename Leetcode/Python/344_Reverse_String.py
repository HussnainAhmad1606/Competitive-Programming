class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        index = 0
        for i in range(0, length):
            str1 = s.pop()
            s.insert(index,str1)
            index = index+1
        print(s)
            
        
                
result = Solution()
input1 = ["H","a","n","n","a","h"]
res = result.reverseString(input1)
print(res)
        
