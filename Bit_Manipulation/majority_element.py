#array | divide-and-conquer | bit-manipulation
# adobe | zenefits
class Solution:
    def majorityElement(self, nums):
        num_dict={} # empty nums dictionary
        for n in nums:
            if n not in num_dict:
                num_dict[n]=1
            else:
                num_dict[n]+=1
            if num_dict[n]>len(nums)/2:
                return n
if __name__ == '__main__':
    s=Solution()
    nums=list(map(int,input().strip().split()))
    result= s.majorityElement(nums)
    print(result)