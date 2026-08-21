import math
from typing import List


class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Inclusion-Exclusion Principle से x तक कुल कितने multiple हैं, गिनने का फंक्शन
        def count(x: int) -> int:
            total_count = 0

            # coins के सभी subset combinations जनरेट करना (Bitmasking)
            for i in range(1, 1 << n):
                lcm_val = 1
                bits_set = 0

                for j in range(n):
                    if (i >> j) & 1:
                        bits_set += 1
                        lcm_val = math.lcm(lcm_val, coins[j])

                # Odd set bits पर जोड़ें (+), Even set bits पर घटाएं (-)
                if bits_set % 2 == 1:
                    total_count += x // lcm_val
                else:
                    total_count -= x // lcm_val

            return total_count

        # Binary Search Range
        left = 1
        right = min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans