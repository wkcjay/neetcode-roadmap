from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        stack = deque()
        if len(s)//2 == 0:
            return False
        for item in s:
            if item not in mapping:
                stack.append(item)
            elif len(stack) == 0 or stack.pop() != mapping[item]:
                return False
        if len(stack) != 0:
            return False
        return True