class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        count=0
        for n in numSet:
            if (n-1) not in numSet:
                length=0
                while (n+length) in numSet:
                    length+=1
                count=max(length,count)
        return count
        
