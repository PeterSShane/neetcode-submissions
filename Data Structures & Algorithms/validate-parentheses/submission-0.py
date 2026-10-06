class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {'{':'}', '(':')', '[':']'}

        for char in s:
            if char in dict:
                stack.append(char)
            else:
                if not stack:
                    return False
                if dict[stack.pop()] != char:
                    return False
        
        return len(stack) == 0

