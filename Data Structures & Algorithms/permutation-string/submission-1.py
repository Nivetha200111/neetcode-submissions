class Solution:
    def checkInclusion(self, str1: str, str2: str) -> bool:
        for i in range(len(str2)):
            window = str2[i:i+len(str1)]
            if sorted(window) == sorted(str1):
                return True
        return False