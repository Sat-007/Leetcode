class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
    
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                cur = ""
                while stack and stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()
                
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(cur * int(num))
        return "".join(stack)                
                
            