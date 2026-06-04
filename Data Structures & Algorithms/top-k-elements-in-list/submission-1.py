class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        pq = []
        for n, c in count.items():
            heapq.heappush(pq, (c, n))
            if len(pq) > k:
                heapq.heappop(pq)

        return [n for c, n in pq]