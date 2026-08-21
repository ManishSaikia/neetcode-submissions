from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        heap = []

        for key, value in freq.items():
            if len(heap) < k or value > heap[0][0]:
                heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]
        
