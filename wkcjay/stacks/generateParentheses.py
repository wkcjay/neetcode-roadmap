from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid if open == closed == n
        stack = deque()
        res = []
        def backtracking(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN + 1)
                stack.pop()

        backtracking(0, 0)
        return res