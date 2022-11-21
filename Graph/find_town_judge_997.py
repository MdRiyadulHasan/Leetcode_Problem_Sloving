from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust) -> int:
        trust_to = defaultdict(int)
        trusted = defaultdict(int)
        for a,b in trust:
            trust_to[a]+=1
            trusted[b]+=1
        for i in range(1,n+1):
            if trust_to[i]==0 and trusted[i]==n-1:
                return i
        return -1
if __name__ == '__main__':
    n=3
    trust = [[1,3],[2,3]]
    ob = Solution()
    ans = ob.findJudge(n,trust)
    print(ans)