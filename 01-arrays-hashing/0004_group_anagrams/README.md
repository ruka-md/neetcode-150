
# 0004 - Group Anagrams

## 🧠 Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

**Example:**
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


**Constraints:**
- 1 <= strs.length <= 10⁴
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

---

## 🛠️ Approach

### Method 1: Sort Each Word
- Sort each word alphabetically to create a common key (e.g., `'eat'` → `'aet'`)
- Use this sorted string as a key in a dictionary
- Append the original word to the corresponding group

### Method 2: Character Count as Key (Optimized)
- For each word, count the occurrences of each letter (`a` to `z`)
- Use the 26-length count tuple as a dictionary key
- Append the word to the group corresponding to this signature

Example for `"abb"` → key = `(1, 2, 0, ..., 0)`

---

## 🔄 Key Differences

- **Sorted Key**: Simple to understand and implement, but `O(k log k)` per word due to sorting.
- **Count Key**: Faster (`O(k)`), ideal for longer words or performance-critical cases.
- **Robustness**: Both methods handle edge cases correctly and are suitable for interview use.

---

## ⏱️ Time Complexity

| Method             | Time           | Space        |
|--------------------|----------------|--------------|
| Sort Key           | O(n * k log k) | O(n * k)     |
| Count Key (Tuple)  | O(n * k)       | O(n * k)     |

- `n` = number of words in `strs`  
- `k` = maximum length of a single word
