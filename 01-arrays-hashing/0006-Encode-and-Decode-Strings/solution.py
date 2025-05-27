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
