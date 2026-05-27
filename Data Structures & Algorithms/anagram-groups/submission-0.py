from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        
        strs_map = defaultdict(list)

        for word in strs:
            key = "".join((sorted(word)))
            
            strs_map[key].append(word)
        
        return list(strs_map.values())