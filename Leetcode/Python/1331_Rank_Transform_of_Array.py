class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rankDict = {}
        arrSort = sorted(arr)
        rank = 1
        for i in range(len(arrSort)):
            if i > 0 and arrSort[i] > arrSort[i - 1]:
                rank += 1
            rankDict[arrSort[i]] = rank
        for i in range(len(arr)):
            arr[i] = rankDict[arr[i]]
        return arr

sol = Solution()
arr = []
res = sol.arrayRankTransform(arr)
print(res)
