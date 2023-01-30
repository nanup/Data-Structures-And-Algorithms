from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        
        for parenthesis in s:
            if parenthesis in "({[":
                stack.append(parenthesis)
            else:
                if not stack:
                    return False
                
                prevParenthesis = stack.pop()
                
                if (parenthesis == ")" and prevParenthesis != "(") or \
                   (parenthesis == "}" and prevParenthesis != "{") or \
                   (parenthesis == "]" and prevParenthesis != "["):
                    return False
        if stack:
            return False
        return True