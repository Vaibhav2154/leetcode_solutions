class Solution:
    def reverse(self, x: int) -> int:
        isneg = x < 0
        x = abs(x)
        rev = 0
        rem = 0
        while x:
            rem = x%10
            rev = rev*10+rem
            x = x//10

        if rev < -2**31 or rev > 2**31 - 1:
            return 0
            
        return -1*rev if isneg else rev