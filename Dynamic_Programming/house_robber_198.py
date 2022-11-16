def rob(nums) -> int:
    rob1=0
    rob2=0
    for n in nums:
        temp=max(rob1+n, rob2)
        rob1 = rob2
        rob2=temp
    return rob2
if __name__ == '__main__':
    nums =[1,2,3,1]
    ans=rob(nums)
    print(ans)

        