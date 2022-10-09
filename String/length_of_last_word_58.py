class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        length=0
        while s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            length+=1
            i-=1 
        return length
if __name__ =="__main__":
    ob=Solution()
    s=input()
    ans=ob.lengthOfLastWord(s)
    print(ans)