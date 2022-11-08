# math
# apple | bloomberg 
import math
def reverse( x: int) -> int:
    Max=2147483647
    Min = -2147483648
    res=0
    while x:
        rem=int(math.fmod(x,10))
        x=int(x/10)
        if (res>Max//10 or (res==Max//10 and rem>=Max%10)):
            return 0
        if (res<Min//10 or (res==Min//10 and rem<=Min%10)):
            return 0
        res=res*10 + rem
    return res    
if __name__ == '__main__':
    x=-2147483649
    ans =reverse(x)
    print(ans)
   