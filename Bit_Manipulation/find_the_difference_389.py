class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result=0
        for cs in s:
            result=result^ord(cs)
        for ct in t:
            result=result^ord(ct)
        return chr(result)
if __name__ == '__main__':
    s=input()
    t=input()
    ob=Solution()
    ans=ob.findTheDifference(s,t)
    print(ans)