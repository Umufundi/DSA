class Solution:
    def findNthDigit(self, n: int) -> int:
        # Step 1: Determine the length of the number
        length, count, start = 1, 9, 1

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        # Step 2: Find the actual number where the nth digit is located
        start += (n - 1) // length

        # Step 3: Extract the nth digit from that number
        return int(str(start)[(n - 1) % length])