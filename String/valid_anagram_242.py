# hash-table | sort
# amazon | uber | yelp
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)