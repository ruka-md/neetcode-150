# 0005 - Top K Frequent Elements

---

## 🧠 Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.  
You may return the answer in **any order**.

---

## 🧪 Examples
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Input: nums = [1], k = 1
Output: [1]


---

## 🛠️ Approaches

### ✅ Approach 1: Counter + sorted

- Count frequencies using `collections.Counter`
- Use `sorted(..., key=..., reverse=True)` to sort elements by frequency
- Extract the top `k` frequent elements

**Time Complexity:** O(N log N)  
**Space Complexity:** O(N)

---

### ✅ Approach 2: Counter + heapq (min-heap)

- Count frequencies using `collections.Counter`
- Use `heapq` to maintain a min-heap of the top `k` frequent elements
- Push `(-freq, num)` into heap to simulate max-heap behavior

**Time Complexity:** O(N log k)  
**Space Complexity:** O(N)

---

## 🏷️ Tags

`Hash Map`, `Heap (Priority Queue)`, `Sorting`

