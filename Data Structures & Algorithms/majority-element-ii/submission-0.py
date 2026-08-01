class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        ans=[]
        n=len(nums)
        for item in nums:
            freq[item]=freq.get(item,0)+1
        for key,value in freq.items():
            if value>n//3:
                ans.append(key)
        return ans


        