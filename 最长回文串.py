import collections

"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
"""

def solution(s: str):
    ans = 0
    flag = False
    count = collections.Counter(s)
    # for i in s:
    #    if i in d:
    #         d[i] += 1
    #     else:
    #         d[i] = 1
    for v in count.values():
        if v % 2 == 0:
            ans += v
        else:
            ans += v -1
            flag = True
    if flag:
        ans += 1
    return ans

print(solution("abccccdd"))