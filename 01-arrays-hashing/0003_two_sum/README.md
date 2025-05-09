# 0003 - Two Sum

### 🧠 Problem

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.

Return the answer with the smaller index first.

---

### 🛠️ Approach

#### Method 1: Hash Map

- Store each visited number and its index in a dictionary.
- For each number, check if `target - num` exists in the dictionary.
- If found, return the stored index and current index.

#### Method 2: Two Pointers after Sorting

- Pair each number with its index: `[(num, idx) for idx, num in enumerate(nums)]`
- Sort the list by value: `sorted_nums.sort()`
- Use `while` instead of `for` to move inward from both ends until the pair is found.

---

### 🔁 Key Differences

- **Hash Map**: No sorting needed, works in original order.
- **Two Pointers**: Requires sorting, but efficient for sorted input.
- **Complexity difference**: Hash map is O(n), two pointers is O(n log n) due to sort.

---

### ⏱️ Time Complexity

| Method      | Time       | Space  |
|-------------|------------|--------|
| Hash Map    | O(n)       | O(n)   |
| Two Pointers| O(n log n) | O(n)   |
