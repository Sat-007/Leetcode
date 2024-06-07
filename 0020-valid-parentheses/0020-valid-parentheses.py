class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        paren = {")":"(","}":"{","]":"["}
        
        for p in s:
            if p in paren.values():
                stack.append(p)
            elif stack and paren[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []