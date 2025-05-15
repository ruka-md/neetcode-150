# notes.md
"""
# Notes: Top K Frequent Elements

## Problem
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

---

## Key Learnings

### ✅ Understanding Counter
- `Counter(nums)` creates a dictionary-like object `{element: frequency}`.
- Using `.items()` converts it into `(key, value)` tuples, which allow sorting by value.
- Once converted to tuples, `key` and `value` are treated equally — enabling `lambda x: x[1]` to sort by frequency.

### ✅ Sorting Behavior
- `sorted(counter)` only sorts by key (the elements themselves), not frequency.
- To sort by frequency, use `.items()` and `key=lambda x: x[1]`.
- Use `reverse=True` to sort in descending order (most frequent first).

### ✅ heapq Basics
- `heapq` is a min-heap by default.
- To simulate a max-heap, insert `(-freq, num)` instead of `(freq, num)`.
- Call `heapq.heapify()` to turn a list into a heap.
- `heapq.heappop()` retrieves the smallest item (i.e., highest frequency due to negation).
- Tuples are compared by their first elements, allowing custom priority logic like `(priority, value)`.

### ✅ heapq vs sorted
- `sorted()` takes O(N log N), while `heapq` can do the job in O(N log k).
- When N is large and k is small, `heapq` is more efficient.
- For simplicity, `heapq.nlargest(k, counter.items(), key=lambda x: x[1])` is a clean one-liner.

---

## Summary
- `.items()` is essential for value-based operations like sorting or heap processing.
- Without `reverse=True`, `sorted()` returns ascending order, which doesn't suit top-k extraction.
- `heapq` requires negating frequency for max-heap simulation.
- This is a foundational pattern for solving top-k frequency problems efficiently.
"""
