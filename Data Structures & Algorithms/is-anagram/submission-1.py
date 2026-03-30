class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = {}
        dicT = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                dicS[s[i]] = dicS.get(s[i], 0) + 1
                dicT[t[i]] = dicT.get(t[i], 0) + 1
            return dicS == dicT