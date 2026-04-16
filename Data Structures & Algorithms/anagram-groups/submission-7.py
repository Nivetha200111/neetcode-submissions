class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1 #find if its anagrom
            res[tuple(count)].append(word) # add it in hashable list if its an anagram add it to an anagram group - based on the count. since all else is zero if its a new word it gets added 
        return list(res.values())