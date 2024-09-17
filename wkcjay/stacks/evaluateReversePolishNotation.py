from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = deque()
        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                val1, val2 = stack.pop(), stack.pop()
                stack.append(int(eval(f"{val2} {item} {val1}")))
        return stack.pop()