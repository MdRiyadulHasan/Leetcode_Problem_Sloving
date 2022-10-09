# string
# yelp
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix=''
        for i in range(len(strs[0])):
            for s in strs:
                if i==len(s) or s[i]!=strs[0][i]:
                    return prefix
            prefix=prefix+strs[0][i]
        return prefix
if __name__ =="__main__":
    ob=Solution()
    strs=list(map(str,input().strip().split()))
    ans=ob.longestCommonPrefix(strs)
    print(ans)
