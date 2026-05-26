from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slen = len(s)
        tlen = len(t)
        if slen != tlen:
            return False
        
        scount = Counter(s)
        tcount = Counter(t)

        if scount == tcount:
            return True
        else:
            return False
