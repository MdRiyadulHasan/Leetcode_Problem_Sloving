class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        people.sort()
        l,r=0,len(people)-1
        boats=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l=l+1
                r=r-1
            else:
                r=r-1
            boats=boats+1
        return boats