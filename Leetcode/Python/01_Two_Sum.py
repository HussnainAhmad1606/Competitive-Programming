class Solution:
    def twoSum(self, array, target):
        index = 0
        while (index<=len(array)):
            for i in range(index+1, len(array)):
                if (array[index]+array[i] == target):
                    return [index, i]

            index += 1