# Notes: 0004 - Group Anagrams

---

## 🔁 Character Count → Tuple Technique

Use this technique when the order of characters doesn’t matter,  
but the character composition (type + frequency) must match exactly.

    count = [0] * 26
    for c in word:
        count[ord(c) - ord('a')] += 1
    key = tuple(count)

- `ord(c) - ord('a')` maps `'a'` to `0`, `'z'` to `25`  
- `tuple(count)` is hashable and usable as a dictionary key  
- Runs in `O(k)` per word (faster than sorting)

---

## 🔤 Converting sorted(word) to string

    sorted("word")            # → ['d', 'o', 'r', 'w']
    ''.join(sorted("word"))   # → 'dorw'

---

## 📦 Getting values from a dictionary

    list(my_dict.values())  # → List[List[str]]

---

## 🧰 Using defaultdict(list)

    from collections import defaultdict
    my_dict = defaultdict(list)
    my_dict[key].append(word)

---

## ⚠️ Dictionary key rules

❌ Invalid:
- `list` → unhashable

✅ Valid:
- `''.join(sorted(word))` → string  
- `tuple(sorted(word))` → tuple of characters  
- `tuple(count)` → tuple of 26 integers
