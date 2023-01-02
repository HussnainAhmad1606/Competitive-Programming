class Solution:
    def isPalindrome(self, s: str):
        nonCharacters = ['.', ',', '!', '@', '#', '&', '(', ')', '-', "_", '[', '{', '}', ']', '|', ':', ';', ',', '?', '/', '\\', '"', "'", '*', '`', '~', '$', '^', '+', '=', '<', '>', " "]
        
        for char in nonCharacters:
            s = s.replace(char, "")
            
        word = s.lower()
        print(word)
        reverse= word[::-1]
        print(reverse)
        if (word==reverse):
            return True
        else:
            return False