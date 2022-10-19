# hash-table | string
# amazon | bloomberg | facebook | uber | yelp
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d=defaultdict(list)
        for word in strs:
            d[tuple(sorted(word))].append(word)
        return list(d.values())