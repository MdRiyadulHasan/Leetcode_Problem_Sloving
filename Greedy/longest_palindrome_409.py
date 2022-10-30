# hash-table
# google
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        odd=False
        res=0
        for k,v in freq.items():
            if v%2==0:
                res=res+v
            else:
                res=res+v-1
                odd=True
        if odd:
            res=res+1
        return res