class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=5
        total=0
        while x<=n:
            total+=n//x
            x*=5
        return total