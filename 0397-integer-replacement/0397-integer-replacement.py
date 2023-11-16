class Solution:
    def integerReplacement(self, n: int) -> int:
        def steps(n, count):
            if n == 1:
                return count

            if n % 2 == 0:
                return steps(n // 2, count + 1)
            else:
                return min(steps(n + 1, count + 1), steps(n - 1, count + 1))

        return steps(n, 0)