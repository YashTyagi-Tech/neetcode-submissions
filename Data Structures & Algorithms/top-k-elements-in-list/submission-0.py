class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for items in nums:
            freq[items]=freq.get(items,0)+1
        # sorted(freq.items())
        sorted_items=sorted(freq.items(),key=lambda item: item[1])
        last_k=sorted_items[-k:]
        return [item[0] for item in last_k]

        