import re
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        string1Alpha = {}
        string2Alpha = {}
        
        for i in range(0, len(alphabets)):
            result = re.findall(alphabets[i], s)
            if len(result) != 0:
                string1Alpha[alphabets[i]] = len(result)
                
        for i in range(0, len(alphabets)):
            result = re.findall(alphabets[i], t)
            if len(result) != 0:
                string2Alpha[alphabets[i]] = len(result)
                
        if (string1Alpha == string2Alpha):
            return True
        return False
                
result = Solution()
str1 = "rat"
str2 = "car"
res = result.isAnagram(str1, str2)
print(res)
        
