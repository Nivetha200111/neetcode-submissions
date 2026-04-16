class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s)!= len(t):
            return False
        for char in s:
            count[char] = count.get(char,0)+1
        for char in t:
            if char in count:
                count[char] = count.get(char,0)-1
        for s in count.values():
            if s!=0:
                return False
        return True
        