class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        t= re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if t == t[::-1]:
            return True
        return False