# 0003 - Two Sum

## Summary

Return the indices of the two numbers such that they add up to the target.  
Return the answer with the smaller index first.

### 🧠 Key Insight

#### 🔸 Two Pointers
- Use `while` instead of `for` to allow dynamic movement of both ends.
- Store the original indices by pairing each number with its index:
  - `sorted_nums = [(num, idx) for idx, num in enumerate(nums)]`
  - `sorted_nums.sort()` to sort while preserving original indices.

#### 🔸 Hash Map
- O(n) time complexity by storing visited numbers and checking complements.
- Does not require sorting, making it ideal for unsorted input.

#### 🔁 Difference
- **Hash Map**: O(n) time, O(n) space → optimal for unsorted arrays.
- **Two Pointers**: O(n log n) time (due to sorting), O(n) space.

### 🔍 Complexity

**Two Pointers**
- Time: O(n log n)
- Space: O(n)

**Hash Map**
- Time: O(n)
- Space: O(n)
