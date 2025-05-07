from collections import Counter

# Solution 1: Using Counter (character frequency comparison)
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Solution 2: Using sorted() (sort both strings and compare)
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
