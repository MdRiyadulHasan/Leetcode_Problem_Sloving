from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText=Counter(text)
        count_balloon = Counter("balloon")
        res=len(text)
        for c in count_balloon:
            res=min(res, countText[c]//count_balloon[c])
        return res