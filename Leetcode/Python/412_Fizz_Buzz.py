class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        index = 1
        result = [None] * (n+1)
        result[0] = 0
        while (index <= n):
            if (index%3 == 0):
                if (index%5 == 0):
                    result[index] = "FizzBuzz"
                else:
                    result[index] = "Fizz"
                    
            elif (index%5 == 0):
                result[index] = "Buzz"
            else:
                string2 = str(index)
                result[index] = string2
        
            index = index + 1


        result.pop(0)        
        return result
        
