class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res=0
        left=0
        right=len(people)-1
        while left<=right:
            if people[left]+people[right]>limit:
                right-=1
            else:
                right-=1
                left+=1
            res+=1
        return res
