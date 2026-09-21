class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dici1 = {}
        dici2 = {}

        for ch in s:
            dici1[ch] = dici1.get(ch,0) + 1

        for ch in t:
            dici2[ch] = dici2.get(ch,0) + 1

        return dici1 == dici2