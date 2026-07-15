class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         for i in range(len(nums)):
            if nums.count(nums[i])>len(nums)/2:
                return nums[i]