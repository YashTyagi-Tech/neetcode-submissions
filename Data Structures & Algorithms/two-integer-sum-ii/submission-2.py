class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result=[]
        left=0
        right=len(numbers)-1
        while left<right:
            summ=numbers[left]+numbers[right]
            if summ==target:
                result.append(left+1)
                result.append(right+1)
                return result
            elif summ<target:
                left+=1
            else:
                right-=1