import heapq
from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        total_ops = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # If total operations can reduce all differences to 0, min sum is 0
        if sum(diffs) <= total_ops:
            return 0
            
        counts = Counter(diffs)
        # Use a max-heap (storing negative difference values)
        max_heap = [(-d, count) for d, count in counts.items()]
        heapq.heapify(max_heap)
        
        while total_ops > 0 and max_heap:
            d_neg, count = heapq.heappop(max_heap)
            d = -d_neg
            
            if not max_heap:
                can_reduce = total_ops // count
                remainder = total_ops % count
                new_d = d - can_reduce
                if new_d > 0:
                    heapq.heappush(max_heap, (-new_d, count - remainder))
                    if remainder > 0 and new_d - 1 > 0:
                        heapq.heappush(max_heap, (-(new_d - 1), remainder))
                break
            
            next_d_neg, next_count = max_heap[0]
            next_d = -next_d_neg
            
            diff_steps = (d - next_d) * count
            
            if total_ops >= diff_steps:
                total_ops -= diff_steps
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-next_d, next_count + count))
            else:
                can_reduce = total_ops // count
                remainder = total_ops % count
                new_d = d - can_reduce
                
                heapq.heappush(max_heap, (-new_d, count - remainder))
                if remainder > 0 and new_d - 1 > 0:
                    heapq.heappush(max_heap, (-(new_d - 1), remainder))
                total_ops = 0
                break
                
        res = 0
        for d_neg, count in max_heap:
            d = -d_neg
            res += (d ** 2) * count
            
        return res