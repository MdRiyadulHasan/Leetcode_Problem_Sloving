nums=[5,6,7,8,9,5,10,2,3,6,7,4,3,5,6,7,8]
def gen(numbers):
    for n in numbers:
        yield n*n
my_gen=gen(nums)
for i in my_gen:
    print (i)
print('New Line')
my_gen1 = (n*n for n in nums)
for i in my_gen1:
    print(i)
