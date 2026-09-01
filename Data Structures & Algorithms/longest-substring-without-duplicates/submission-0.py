class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()

        left=0
        max_string=0
        for right in range(0,len(s)):
            while s[right] in char:
                char.remove(s[left])
                left+=1
            char.add(s[right])
            max_string=max(max_string,right-left+1)
        return max_string
            
        