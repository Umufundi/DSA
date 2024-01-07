class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = x ** n
        return float(f'{num:.5f}')
    
        