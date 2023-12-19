class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):  # Adjust the range to include n
            count = 0
            string_representation = bin(i)[2:]
            for bit in string_representation:
                if bit == "1":
                    count += 1
            result.append(count)
        return result