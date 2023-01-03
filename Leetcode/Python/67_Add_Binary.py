class Solution:
    def addBinary(self, a, b):
        answer = ""
        while(len(a) != len(b)):
            if (len(a) > len(b)):
                b = "0" + b
            else:
                a = "0" + a
        i = len(a) - 1
        carry = 0
        while(i>=0):
            if ((i==0) and (len(a) != 1 and len(b) != 1)):
                add = int(a[i]) + int(b[i]) + carry
                
                carry = int(add / 2)
                print(f"Carry: {carry}")
                remainder = add % 2
                answer = str(carry) + str(remainder) + answer
            elif (i==0 and a[i] == "1" and b[i] == "1"):
                add = int(a[i]) + int(b[i])
                carry = int(add / 2)
                print(f"Carry: {carry}")
                remainder = add % 2
                answer = str(carry) + str(remainder)
                
               
            else:
                print(f"First Carry: {carry}")
                add = int(a[i]) + int(b[i]) + carry
                carry = int(add / 2)
                print(f"Carry: {carry}")
                remainder = add % 2
                print(f"Remainder: {remainder}")
                answer = str(remainder) + answer
     
                
            i = i - 1
        
        firstZeros = answer.find("1")
        answer = answer[firstZeros:]
                
            
        return answer
