# filter function
# condition must 
def over_two(nums):
    list1=[x for x in nums if x>2]
    return list1
ans=over_two([2,3,4,5,1])
print(ans)
# filter 
n=[1,2,3,4,5,6,7]
ans=list(filter(lambda x:x>4,n))
print(ans)
my_list = list(filter(lambda x:x%2==0,n))
print(my_list)
