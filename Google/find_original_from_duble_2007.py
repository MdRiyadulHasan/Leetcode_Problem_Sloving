from collections import Counter
def findOriginalArray(changed):
    n=len(changed)
    if n%2:
        return []
    changed.sort()
    count=Counter(changed)
    ans=[]
    for num in changed:
        if num==0 and count[num]>=2:
            count[num]-=2
            ans.append(num)
        elif num>0 and count[num] and count[num*2]:
            count[num]-=1
            count[num*2]-=1
            ans.append(num)
    return ans if len(ans)==n//2 else []
if __name__ == '__main__':
    changed=[6,3,0,1]
    ans =findOriginalArray(changed)
    print(ans)