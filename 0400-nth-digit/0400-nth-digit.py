class Solution:
    def findNthDigit(self, n: int) -> int:
        num,digit = 1,1
        count = 9

        while(n > digit * count):
            n -= digit * count
            digit +=1
            count *= 10
            num *=10

        num += (n-1)//digit
        index = (n-1)%digit
        s = str(num)
        return int(s[index])