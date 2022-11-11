# normal function
def square(nums):
    list1=[]
    for n in nums:
        list1.append(n*n)
    return list1
ans =square([5,6,7,8])
print(ans)

# map 
n=[9,10,11,12]
ans = list(map(lambda x:x**2,n))
print(ans)
