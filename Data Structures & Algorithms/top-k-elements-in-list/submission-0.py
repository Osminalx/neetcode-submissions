import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        top_frequent = heapq.nlargest(k, counts.keys(), key=counts.get)
        
        return top_frequent