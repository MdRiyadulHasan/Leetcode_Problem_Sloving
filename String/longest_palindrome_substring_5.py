# string | dynamic-programming
# amazon | bloomberg | microsoft
def longestPalindrome( s):
    res=''
    reslen=0
    for i in range(len(s)):
        # odd length
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>reslen:
                res=s[l:r+1]
                reslen = r-l+1
            l-=1
            r+=1
        # even length
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1)>reslen:
                res=s[l:r+1]
                reslen = r-l+1
            l-=1
            r+=1
    return res

    
if __name__ == '__main__':
    s="cbbd"
    ans =longestPalindrome(s)
    print(ans)