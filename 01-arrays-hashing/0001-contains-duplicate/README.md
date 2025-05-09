# 0001 - Contains Duplicate

## 🧠 Problem

Given an integer array `nums`, return `true` if any value appears **at least twice**, and `false` if every element is distinct.

---

## Summary

Return True if any value appears more than once in the list.

### 🧠 Key Insight

- A set automatically removes duplicates, making it ideal for this task.
- Comparing `len(set(nums))` to `len(nums)` tells us if duplicates existed.
- Using a dictionary also works (`dict[num] = 1`), but set is simpler and more Pythonic.
- Chose set for its structural clarity and consistency when working with unique values.

### 🔍 Complexity

- Time: O(n)
- Space: O(n)
