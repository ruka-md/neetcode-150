```python
# ------------------------------------------------------------
# 🧠 0271. Encode and Decode Strings
# ------------------------------------------------------------
#
# ✅ Problem
# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.
#
# Implement:
#   - encode(strs: List[str]) -> str
#   - decode(s: str) -> List[str]
#
# ⚠️ Edge cases:
#   - empty strings: ""
#   - strings containing "#"
#
# ------------------------------------------------------------
# ✅ My Approach
# ------------------------------------------------------------
#
# 【Encoding】
# Each word is encoded as:
#     [length of word]#[word]
# For example:
#     ["leet", "code", ""] → "4#leet4#code0#"
#
# 【Decoding】
# - Use a `reading` flag to manage state
# - First, accumulate digits in `num_str` until '#' is reached
# - Then read `count` characters as the word
# - If count is 0, append empty string immediately and skip reading
#
# ------------------------------------------------------------
# ✅ Code
# ------------------------------------------------------------

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

# ------------------------------------------------------------
# ✅ Example
# ------------------------------------------------------------

# sol = Solution()
# data = ["abc", "", "#", "123", "a#b"]
# encoded = sol.encode(data)
# print("Encoded:", encoded)      # e.g. "3#abc0#1##3#1233#a#b"
# decoded = sol.decode(encoded)
# print("Decoded:", decoded)      # ['abc', '', '#', '123', 'a#b']
# assert decoded == data

# ------------------------------------------------------------
# ✅ Time Complexity: O(N)
# ✅ Space Complexity: O(N)
# ------------------------------------------------------------
