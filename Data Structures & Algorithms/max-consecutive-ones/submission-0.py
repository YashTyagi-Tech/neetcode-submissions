class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_ones=0
        max_ones=0
        for i in range(len(nums)):
            if nums[i]==1:
                current_ones+=1
                max_ones=max(max_ones,current_ones)
            else:

                current_ones=0
        return max_ones
        