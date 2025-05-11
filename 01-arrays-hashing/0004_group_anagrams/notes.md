# Notes: 0004 - Group Anagrams

# 🔁 Character Count → Tuple Technique (Anagram Pattern)

# 🧠 When to use it:
# Use this technique when the order of characters doesn't matter,
# but the character composition (type + count) must match exactly.

# 🔸 Typical problems:
# - isAnagram(s, t)
# - groupAnagrams(strs)
# - findAllAnagrams(s, p)
# - permutationInString(s1, s2)

# 🛠️ Pattern:
count = [0] * 26
for c in word:
    count[ord(c) - ord('a')] += 1
key = tuple(count)  # hashable and usable as a dictionary key

# ord(c) - ord('a') maps 'a' to 0, 'b' to 1, ..., 'z' to 25
# tuple(count) is immutable and can be used as a key
# Runs in O(k) time per word (faster than sorting)

# 🧩 .join() after sorted()

# sorted(word) returns a list of characters
# Use ''.join(...) to turn it back into a string

# ✅ Example:
sorted("word")            # → ['d', 'o', 'r', 'w']
''.join(sorted("word"))   # → 'dorw'

# 📦 Extracting all values from a dictionary
list(dictionary.values())  # → List[List[str]]

# 🧰 Using defaultdict(list)

# Automatically initializes missing keys with empty lists
from collections import defaultdict

dict = defaultdict(list)
dict[key].append(value)  # no need for key existence check

# ⚠️ Dictionary Keys: What you can and can't use

# ❌ Cannot use list as a dictionary key (unhashable)
# ✅ Can use:
# - ''.join(sorted(word)) → string
# - tuple(sorted(word))   → tuple of characters
# - tuple(count)          → tuple of 26 integers (a-z counts)
