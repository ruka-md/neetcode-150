# 0271. Encode and Decode Strings

## Problem

Design an algorithm to encode a list of strings to a single string.  
The encoded string is then decoded back to the original list of strings.

You must implement:
- `encode(strs: List[str]) -> str`
- `decode(s: str) -> List[str]`

## Constraints

- The list may contain empty strings or strings with special characters like `#`.
- The encoded format must be lossless and fully decodable.

## Approach

- Each string is encoded as: `[length of string]#[string content]`
- This ensures `#` in the content doesn't interfere with decoding.
- The decoder uses a state-based approach (`reading` flag) to switch between reading the length and reading the content.

## Example

```python
sol = Solution()
data = ["abc", "", "#", "123", "a#b"]
encoded = sol.encode(data)
print("Encoded:", encoded)
decoded = sol.decode(encoded)
print("Decoded:", decoded)
assert decoded == data
