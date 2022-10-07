# bit-manipulation
# facebook
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        sol=x^y
        count=0
        for i in range(32):
            if sol&1:
                count=count+1
            sol>>=1
        return count
if __name__ == '__main__':
    x=int(input())
    y=int(input())
    s=Solution()
    ans=s.hammingDistance(x,y)
    print(ans)