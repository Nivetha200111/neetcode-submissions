class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        str1_count = {}
        win_count = {}
        if len(s1) > len(s2): return False
        for char in s1:
            str1_count[char] = str1_count.get(char,0) + 1
        for i in range(len(s1)):
            char = s2[i]
            win_count[char] = win_count.get(char,0) + 1

        if win_count == str1_count:
            return True
        for i in range(len(s1),len(s2)):
            newchar = s2[i]
            win_count[newchar] = win_count.get(newchar,0) + 1

            old_char = s2[i - len(s1)]
            win_count[old_char] -= 1

            if win_count[old_char] == 0:
                del win_count[old_char]
            if win_count == str1_count:
                return True
        return False
            