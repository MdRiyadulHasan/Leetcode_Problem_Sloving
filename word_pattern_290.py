# hash-table
# dropbox | uber
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split(' ')
        d={}
        if len(pattern)!=len(word):
            return False
        if len(set(pattern))!=len(set(word)):
            return False
        for i in range (len(word)):
            if pattern[i] not in d:
                d[pattern[i]]=word[i]
            elif d[pattern[i]]!=word[i]: # value not same means a=dog and a=cat
                return False
        return True