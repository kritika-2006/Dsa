def find_anagram_indices(s, p):
    result = []
    
    # Direct p ki length jitni window slicing aur compare!
    for i in range(len(s)):
        if sorted(s[i : i + len(p)]) == sorted(p):
            result.append(i)
            
    return result

print(find_anagram_indices("cbaebabacd", "abc"))