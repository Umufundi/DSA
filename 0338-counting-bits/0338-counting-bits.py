class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            # Use the fact that countBits(i) = countBits(i // 2) + (i % 2)
            result[i] = result[i // 2] + (i % 2)
        return result