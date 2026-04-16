class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # move l forward if not alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # move r backward if not alphanumeric
            while l < r and not s[r].isalnum():
                r -= 1

            # now both s[l] and s[r] are alphanumeric, compare lowercase
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
