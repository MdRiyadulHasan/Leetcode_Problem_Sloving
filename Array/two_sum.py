# array | hash-table
# adobe | airbnb | amazon | apple | bloomberg | dropbox | facebook | linkedin | microsoft | uber | yahoo | yelp
class Solution:
    def twoSum(self, nums, target):
        hash_map={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in hash_map:
                return [hash_map[diff],i]
            hash_map[n]=i
if __name__ == '__main__':
    s=Solution()
    target=int(input())
    nums=list(map(int,input().strip().split()))
    result= s.twoSum(nums,target)
    print(result)