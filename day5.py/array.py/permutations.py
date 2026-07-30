def find_anagram_indices(s, p):
    
    
    result = []
    k = len(p)
        
        # 1. Sabse pehle 'p' me 'a' se 'z' tak sabhi letters ki frequency count bana lo (26 letters)
    p_freq = [p.count(chr(c)) for c in range(97, 123)]
        
        # 2. Window ki shuruat 's' ki pehli window se karo
    window_freq = [s[:k].count(chr(c)) for c in range(97, 123)]
        
        # Pehli window check
    if window_freq == p_freq:
            result.append(0)
            
        # 3. Slide the window: ek element add karo, ek remove karo
            for i in range(k, len(s)):
            # Purana element hatao (Left edge)
                left_char_index = ord(s[i - k]) - 97
                window_freq[left_char_index] -= 1
            
            # Naya element jodo (Right edge)
                right_char_index = ord(s[i]) - 97
                window_freq[right_char_index] += 1
            
            # Agar dono 26-length lists same hain, toh index save karo
                if window_freq == p_freq:
                    result.append(i - k + 1)
                
    return result
print(find_anagram_indices("cbaebabacd", "abc"))