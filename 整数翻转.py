class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
            return res if res < (2**31-1) else 0
        else:
            res = int("-" + str(abs(x))[::-1])
            return res if (-2**31) < res else 0


if __name__ == "__main__":
    print(2**31-1)
    print(-2**31)
    a = Solution()
    b = a.reverse(0)
    print(b)
