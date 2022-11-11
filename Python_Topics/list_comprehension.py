# Normal
res=[]
letter='abcd'
for c in letter:
    for n in range(1,5):
        res.append((c,n))
print(res)

# list comprehension
my_list = [(c,n) for c in letter for n in range(1,5)]
print('\n')
print(my_list)

names=['Riyad','Rana','Mohim','Noyan','Hridoy','Shohag']
dept =['CSE','EEE','ME','CE','GCE','IPE']
print (list(zip(names,dept)))

# dictionary
my_dict={}
for name, d in zip(names, dept):
    my_dict[name]=d
print(my_dict)
# dict comprehension
dict1={name:department for name,department in zip(names,dept)}
print(dict1)

numbers=[88,85,88,90,92,92,87,85,93,95,93,87,90,95]

my_set = set()
for n in numbers:
    my_set.add(n)
print(my_set)
# set comprehension
my_set1 = {n for n in numbers}
print(my_set1)

