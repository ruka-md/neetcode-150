```python
# Notes: 0004 - Group Anagrams

# ===================================================
# 🔁 Technique: Character Count → Tuple as a Dict Key
# ===================================================

# ✅ Use when:
# - Order of characters does not matter
# - You care about the exact character composition (type + frequency)

# 🧩 Common problems:
# - isAnagram(s, t)
# - groupAnagrams(strs)
# - findAllAnagrams(s, p)
# - permutationInString(s1, s2)

# 🛠️ Template:
count = [0] * 26
for c in word:
    count[ord(c) - ord('a')] += 1
key = tuple(count)

# Explanation:
# - ord(c) - ord('a') maps 'a' to 0, ..., 'z' to 25
# - tuple(count) is hashable and usable as a dictionary key
# - This approach runs in O(k) per word (faster than sorting)


# ===================================================
# 🔤 Using sorted(word) and join()
# ===================================================

# sorted(word) returns a list of characters
# Use ''.join(...) to turn it back into a string

# ✅ Example:
sorted("word")            # → ['d', 'o', 'r', 'w']
''.join(sorted("word"))   # → 'dorw'


# ===================================================
# 📦 Getting all values from a dictionary
# ===================================================

# dictionary.values() gives all the grouped lists
list(dictionary.values())  # → List[List[str]]


# ===================================================
# 🧰 Using defaultdict(list)
# ===================================================

# Automatically initializes missing keys with empty lists
from collections import defaultdict

group_map = defaultdict(list)
group_map[key].append(word)


# ===================================================
# ⚠️ Dictionary Keys - What you can and can't use
# ===================================================

# ❌ Invalid as key:
# - list (e.g., ['a', 'b']) → unhashable

# ✅ Valid keys:
# - ''.join(sorted(word)) → string
# - tuple(sorted(word))   → tuple of characters
# - tuple(count)          → tuple of 26 integers
```
