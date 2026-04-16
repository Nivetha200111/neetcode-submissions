class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictt = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch not in dictt.keys():
                stack.append(ch)
            elif stack and dictt[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
