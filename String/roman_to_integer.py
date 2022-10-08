class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,
               "M":1000,
        }
        result=0
        length = len(s)
        for i in range (length):
            if i+1<length and roman[s[i]]<roman[s[i+1]]:
                print(roman[s[i]])
                result=result-roman[s[i]]
            else:
                result=result+roman[s[i]]
        return result
if __name__ == '__main__':
    ob=Solution()
    s=input()
    ans=ob.romanToInt(s)
    print(ans)
