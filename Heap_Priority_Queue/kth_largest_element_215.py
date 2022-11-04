# divide-and-conquer | heap
# amazon | apple | bloomberg | facebook | microsoft | pocketgems
import heapq
def findKthLargest( nums, k):
    # minheap
    nums=[-x for x in nums]
    heapq.heapify(nums)
    for i in range(k-1):
        heapq.heappop(nums)
    return -heapq.heappop(nums)
    # quickselect 
    k=len(nums)-k 
    def quickselect(l,r):
        p=l 
        pivot = nums[r] 
        for i in range(l,r):
            if nums[i]<=pivot:
                nums[p],nums[i]=nums[i],nums[p]
                p+=1
        nums[p],nums[r]=nums[r],nums[p]
        if p>k: 
            return quickselect(l,p-1)
        elif p<k:
            return quickselect(p+1,r)
        else:
            return nums[p]
    return quickselect(0,len(nums)-1)

    
if __name__ == '__main__':
    nums=[3,2,3,1,2,4,5,5,6]
    k=4
    ans =findKthLargest(nums,k)
    print(ans)
   