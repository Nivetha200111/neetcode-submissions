class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res=res+str(len(s))+"$"+s;
        return res

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            leng = int(s[i:j])
            arr.append(s[j+1:j+1+leng])
            i = j + 1 + leng
        return arr

