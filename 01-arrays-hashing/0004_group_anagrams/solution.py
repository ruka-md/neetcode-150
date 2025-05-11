from typing import List
from collections import defaultdict

class Solution:
    # Method 1: Use sorted string as dictionary key
    def groupAnagrams_sort(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word and use it as a key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

    # Method 2: Use character count tuple as dictionary key (faster)
    def groupAnagrams_count(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Count frequency of each character (a-z)
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
