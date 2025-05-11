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

# Why it works:
# - ord(c) - ord('a') maps 'a' to 0, ..., 'z' to 25
# - tuple(count) is hashable and usable as a dict key
# - Faster than sorting: O(k) per word

# ===================================================
# 🔤 Handling sorted(word) → back to string
# ===================================================

# sorted(word) returns a list of characters
# ''.join(...) turns it back into a string

# ✅ Example:
sorted("word")            # → ['d', 'o', 'r', 'w']
''.join(sorted("word"))   # → 'dorw'

# ===================================================
# 📦 Extracting grouped results from a dictionary
# ===================================================

# dictionary.values() gives all the grouped lists
list(dictionary.values())  # → List[List[str]]

# ===================================================
# 🧰 Safe grouping with defaultdict(list)
# ===================================================

# No need to check key existence
from collections import defaultdict

group_map = defaultdict(list)
group_map[key].append(word)

# ===================================================
# ⚠️ Dict key types: what you can and can't use
# ===================================================

# ❌ list → NOT hashable, cannot be used as key
# ✅ Allowed keys:
# - ''.join(sorted(word)) → string
# - tuple(sorted(word))   → tuple of characters
# - tuple(count)          → tuple of 26 ints (char frequencies)
