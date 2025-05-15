from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent_sort(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 1: Counter + sorted
        Time Complexity: O(N log N)
        """
        counter = Counter(nums)
        counter_sorted = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in counter_sorted[:k]]

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """
        Approach 2: Counter + heapq (max frequency top-k)
        Time Complexity: O(N log k)
        """
        counter = Counter(nums)
        heap = [(-freq, num) for num, freq in counter.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
