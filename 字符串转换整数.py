import re


class Solution:
    def myAtoi(self, str: str) -> int:
        new = str.lstrip()
        print(new)
        x = ""
        if new[0] == "-":
            x += new[0]
            a = re.match(r'\d+', new[1:]).group()
            x += a
        a = re.match(r'\d+', new[1:]).group()

        print("a的值：", a)
        if a:
            print(a)
        else:
            print("0")


if __name__ == "__main__":
    Solution().myAtoi(" -12")
