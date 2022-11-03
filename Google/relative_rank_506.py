def findRelativeRanks( score):
    sc=sorted(score,reverse=True)
    count={}
    res=[]
    for i in range(len(sc)):
        if i==0:
            count[sc[i]]='Gold Medal'
        elif i==1:
            count[sc[i]]='Silver Medal'
        elif i==2:
            count[sc[i]]='Bronze Medal'
        else:
            count[sc[i]]=str(i+1)
    for num in score:
        res.append(count[num])
    return res
if __name__ == '__main__':
    score=[10,3,8,9,4]
    ans =findRelativeRanks(score)
    print(ans)