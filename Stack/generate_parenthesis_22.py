# string | backtracking
# google | uber | zenefits
class Solution:
    def generateParenthesis(self, n: int):
        stack=[]
        res=[]
        def backtrack(openN,closedN):
            if openN==closedN==n:
                return res.append(''.join(stack))
            if openN<n:
                stack.append('(')
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(')')
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0,0)
        return res