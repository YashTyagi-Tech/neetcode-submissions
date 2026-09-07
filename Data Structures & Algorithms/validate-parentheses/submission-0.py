class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=='(':
                stack.append(')')
            elif ch=='{':
                stack.append('}')
            elif ch=='[':
                stack.append(']')
            elif not stack or stack.pop()!=ch:
                return False
        return not stack
            