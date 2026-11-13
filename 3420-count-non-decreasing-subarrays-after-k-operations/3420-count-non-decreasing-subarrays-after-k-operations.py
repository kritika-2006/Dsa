class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Next greater element to the right
        nxt = [n] * n
        st = []

        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()

            nxt[i] = st[-1] if st else n
            st.append(i)

        # Prefix sum
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        LOG = n.bit_length()

        # Binary lifting tables
        jump = [nxt]
        cost = [[0] * n]

        for i in range(n):
            j = nxt[i]
            cost[0][i] = nums[i] * (j - i) - (pref[j] - pref[i])

        for b in range(1, LOG):
            prev_jump = jump[-1]
            prev_cost = cost[-1]

            nj = [n] * n
            nc = [0] * n

            for i in range(n):
                mid = prev_jump[i]

                if mid < n:
                    nj[i] = prev_jump[mid]
                    nc[i] = prev_cost[i] + prev_cost[mid]
                else:
                    nc[i] = prev_cost[i]

            jump.append(nj)
            cost.append(nc)

        # Calculate operations needed for nums[l:r+1]
        def get_cost(l, r):
            ans = 0
            cur = l

            for b in range(LOG - 1, -1, -1):
                nxt_pos = jump[b][cur]

                if nxt_pos <= r:
                    ans += cost[b][cur]
                    cur = nxt_pos

            ans += nums[cur] * (r - cur + 1)
            ans -= pref[r + 1] - pref[cur]

            return ans

        # Sliding window
        left = 0
        ans = 0

        for right in range(n):
            while left <= right and get_cost(left, right) > k:
                left += 1

            ans += right - left + 1

        return ans