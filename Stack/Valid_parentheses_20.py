# string | stack
# airbnb | amazon | bloomberg | facebook | google | microsoft | twitter | zenefits
class Solution:
    def isValid(self, s):
        stack=[]
        par_map={")":"(", "}":"{", "]":"["}
        open_par=set(["(","{","["])
        for x in s:
            if x in open_par:
                stack.append(x)
            elif stack and stack[-1]==par_map[x]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True
if __name__ == '__main__':
    ob=Solution()
    s=input()
    ans=ob.isValid(s)
    print(ans)