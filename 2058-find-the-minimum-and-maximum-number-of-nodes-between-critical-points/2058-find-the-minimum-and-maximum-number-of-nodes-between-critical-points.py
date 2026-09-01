# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Linked List me kam se kam 3 nodes hone chahiye critical points ke liye
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1
        
        first_critical = -1
        prev_critical = -1
        min_distance = float('inf')
        
        while curr.next:
            # Check for Local Minima or Local Maxima
            is_local_min = curr.val < prev.val and curr.val < curr.next.val
            is_local_max = curr.val > prev.val and curr.val > curr.next.val
            
            if is_local_min or is_local_max:
                if first_critical == -1:
                    first_critical = index
                else:
                    # Adjacent critical points ke beech ka minimum distance update karein
                    min_distance = min(min_distance, index - prev_critical)
                
                prev_critical = index
            
            prev = curr
            curr = curr.next
            index += 1
            
        # Agar 2 se kam critical points mile ho
        if first_critical == -1 or prev_critical == first_critical:
            return [-1, -1]
        
        # Maximum distance pehle aur aakhri critical point ke beech ka hoga
        max_distance = prev_critical - first_critical
        
        return [min_distance, max_distance]