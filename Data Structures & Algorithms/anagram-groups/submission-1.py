class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # l = 0
        # r = l + 1
        # res =[[]]
        # for i in range(len(strs)):
        #     for j in range(i,len(strs)):
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             res.append([strs[i],strs[j]])
        # return strs
        res = defaultdict(list) #mapping character count of each string to the list of anagrams
        for s in strs:
            count = [0] * 26 #each alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        

            