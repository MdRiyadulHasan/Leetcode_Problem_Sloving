def slidingWindow(nums,k):
    maxsum =0
    windowsum = 0
    for i in range(k):
        windowsum+=nums[i]
    maxsum = windowsum
    for j in range(k,len(nums)):
        windowsum = windowsum + nums[j]-nums[j-k]
        maxsum = max(windowsum,maxsum)
    return maxsum
if __name__ == '__main__':
    A = [1,9,-1,-2,7,3,-1,2]
    k=4
    ans = slidingWindow(A,k)
    print(ans)