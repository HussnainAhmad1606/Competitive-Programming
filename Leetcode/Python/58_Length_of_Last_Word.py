class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.strip().split(" ")
        lengthOfWord = len(arr[len(arr)-1])
        return lengthOfWord