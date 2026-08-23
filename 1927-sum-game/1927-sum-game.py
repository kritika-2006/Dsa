class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        left_str = num[:mid]
        right_str = num[mid:]
        
        sum_left = sum(int(ch) for ch in left_str if ch != '?')
        sum_right = sum(int(ch) for ch in right_str if ch != '?')
        
        q_left = left_str.count('?')
        q_right = right_str.count('?')
        
        sum_diff = sum_left - sum_right
        q_diff = q_left - q_right
        
        # Bob wins (False) if difference balances out with average value 4.5
        if sum_diff + q_diff * 4.5 == 0:
            return False
            
        return True