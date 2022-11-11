# normal function
def mx(x,y):
    if x>y:
        return x
    else:
        return y
print(mx(10,5))
# lambda function
big= lambda x,y:x if x>y else y
print(big(20,25))