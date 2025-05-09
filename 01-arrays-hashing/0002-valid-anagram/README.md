# 0002 - Valid Anagram

## 🧠 Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

---

## Summary

Check if two strings are anagrams of each other.

### 🧠 Key Insight

- Sorting both strings and comparing them gives a simple and effective solution.
- Alternatively, use a dictionary or `collections.Counter` to count characters.

### 🔍 Complexity

- Time: O(n log n) for sorting approach
- Space: O(1) if character set is fixed (e.g., only lowercase letters)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
