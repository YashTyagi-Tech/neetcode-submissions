class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq={}
        for i in range(len(nums)):
            if nums[i] not in frq:
                frq[nums[i]]=1
            else:
                frq[nums[i]]+=1
        for x in frq:
            if frq[x]>len(nums)/2:
                return x
             
        
        