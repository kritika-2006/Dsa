import heapq
from collections import defaultdict

class SlidingWindowMedianCost:
    def __init__(self, x):
        self.x = x
        self.small = []  # Max heap (negated values)
        self.large = []  # Min heap
        self.sum_small = 0
        self.sum_large = 0
        self.small_size = 0
        self.large_size = 0
        self.delayed = defaultdict(int)

    def prune(self, heap):
        while heap:
            val = heap[0]
            num = -val if heap is self.small else val
            if self.delayed[num] > 0:
                self.delayed[num] -= 1
                heapq.heappop(heap)
            else:
                break

    def balance(self):
        # Maintain small_size == (x + 1) // 2
        target_small = (self.x + 1) // 2
        
        if self.small_size > target_small:
            val = -heapq.heappop(self.small)
            self.sum_small -= val
            self.small_size -= 1
            heapq.heappush(self.large, val)
            self.sum_large += val
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < target_small and self.large_size > 0:
            self.prune(self.large)
            if self.large:
                val = heapq.heappop(self.large)
                self.sum_large -= val
                self.large_size -= 1
                heapq.heappush(self.small, -val)
                self.sum_small += val
                self.small_size += 1
                self.prune(self.large)

    def add(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.sum_small += num
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.sum_large += num
            self.large_size += 1
        self.balance()

    def remove(self, num):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            self.sum_small -= num
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            self.sum_large -= num
            if self.large and num == self.large[0]:
                self.prune(self.large)
        self.balance()

    def get_cost(self):
        self.prune(self.small)
        median = -self.small[0]
        left_cost = self.small_size * median - self.sum_small
        right_cost = self.sum_large - self.large_size * median
        return left_cost + right_cost

class Solution:
    def minimumOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        costs = [0] * (n - x + 1)
        
        sw = SlidingWindowMedianCost(x)
        for i in range(x):
            sw.add(nums[i])
        costs[0] = sw.get_cost()
        
        for i in range(1, n - x + 1):
            sw.remove(nums[i - 1])
            sw.add(nums[i + x - 1])
            costs[i] = sw.get_cost()
            
        INF = float('inf')
        prev_dp = [0] * (n + 1)
        
        for j in range(1, k + 1):
            curr_dp = [INF] * (n + 1)
            min_prev = INF
            for i in range(j * x, n + 1):
                min_prev = min(min_prev, prev_dp[i - x])
                curr_dp[i] = min(curr_dp[i - 1], min_prev + costs[i - x])
            prev_dp = curr_dp
            
        return prev_dp[n]

    # Platform method aliases
    minOperations = minimumOperations
    solve = minimumOperations