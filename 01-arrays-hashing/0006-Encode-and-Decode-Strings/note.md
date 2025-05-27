"""
# 🧠 0271. Encode and Decode Strings

## Problem
Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

You must implement:
- encode(strs: List[str]) -> str
- decode(s: str) -> List[str]

### Edge Cases
- Empty strings: ""
- Strings containing "#"

---

## Approach

### ✅ Encoding
Each string is encoded as:
    [length]#[content]

Example:
    ["leet", "code", ""] → "4#leet4#code0#"

This format guarantees that even if the content includes "#", 
the decoder can still determine the boundaries using the length prefix.

---

### ✅ Decoding
Use state-based parsing:

- Use a `reading` flag:
    - False: currently reading the number (length of the next word)
    - True: reading the content (the actual word)
- Use `num_str` to accumulate digits until you see `#`
- After `#`, convert `num_str` to int and read exactly `count` characters
- If `count == 0`, append an empty string and skip reading

---

## Code

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(f"{len(word)}#{word}")
        return ''.join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        num_str = ""
        word = ""
        count = 0
        reading = False

        for element in s:
            if not reading:
                if element != "#":
                    num_str += element
                else:
                    count = int(num_str)
                    reading = True
                    num_str = ""
                    word = ""
                    if count == 0:
                        res.append("")
                        reading = False
            else:
                word += element
                count -= 1
                if count == 0:
                    res.append(word)
                    word = ""
                    reading = False
        return res

---

## Example

sol = Solution()
data = ["abc", "", "#", "123", "a#b"]
encoded = sol.encode(data)
print("Encoded:", encoded)  # e.g. "3#abc0#1##3#1233#a#b"
decoded = sol.decode(encoded)
print("Decoded:", decoded)  # ['abc', '', '#', '123', 'a#b']
assert decoded == data

---

## Complexity

- Time: O(N), where N is the total number of characters in all strings
- Space: O(N) for the result
"""
