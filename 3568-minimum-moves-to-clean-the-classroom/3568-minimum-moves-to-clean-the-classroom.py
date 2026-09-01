from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows, cols = len(classroom), len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_pos = []
        
        # Locate Start ('S') and Litters ('L')
        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_pos.append((r, c))
                    
        num_litters = len(litter_pos)
        target_mask = (1 << num_litters) - 1
        litter_map = {pos: i for i, pos in enumerate(litter_pos)}
        
        # Initial check if start position itself is on a litter
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
            
        # Queue state: (r, c, mask, remaining_energy)
        queue = deque([(start_r, start_c, initial_mask, energy)])
        visited = set([(start_r, start_c, initial_mask, energy)])
        
        moves = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            for _ in range(len(queue)):
                r, c, mask, rem_energy = queue.popleft()
                
                if mask == target_mask:
                    return moves
                
                if rem_energy == 0:
                    continue
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and classroom[nr][nc] != 'X':
                        new_mask = mask
                        new_energy = rem_energy - 1
                        
                        # Collect litter
                        if (nr, nc) in litter_map:
                            l_idx = litter_map[(nr, nc)]
                            new_mask |= (1 << l_idx)
                            
                        # Recharge energy only at 'R' station
                        if classroom[nr][nc] == 'R':
                            new_energy = energy
                            
                        state = (nr, nc, new_mask, new_energy)
                        if state not in visited:
                            visited.add(state)
                            queue.append(state)
                            
            moves += 1
            
        return -1