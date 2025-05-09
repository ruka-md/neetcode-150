0003 - Two Sum

Summary

Given an array of integers and a target value, return the indices of the two numbers that add up to the target. Return the answer with the smaller index first.

🧠 Key Insight

🟢 Two Pointers:
- Use `while` instead of `for` to allow dynamic movement of both ends.
- Store the original indices by pairing each number with its index:
  ① `sorted_nums = [(num, idx) for idx, num in enumerate(nums)]`
  ② `sorted_nums.sort()` to sort by value while preserving indices.

🟢 Hash Map:
- Offers O(n) time by storing visited numbers and checking for complements.
- No sorting needed; ideal for unsorted input.

🔁 Difference:
- Hash map: O(n) time and space. Fastest for unsorted input.
- Two pointers: O(n log n) due to sorting. Efficient when array is or can be sorted.

🔍 Complexity

Two Pointers:
- Time: O(n log n)
- Space: O(n)

Hash Map:
- Time: O(n)
- Space: O(n)
