# 0002 - Valid Anagram

## 🧠 Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

## 🧩 Approach

### Method 1: `sorted(s) == sorted(t)`

- Uses built-in `sorted()` to compare sorted characters.
- Simple and intuitive.

### Method 2: Use `collections.Counter`

- Count each character in both strings and compare dictionaries.
- More efficient than sorting.

## ⏱️ Time Complexity

| Method   | Time      | Space     |
|----------|-----------|-----------|
| `sorted` | O(n log n)| O(n)      |
| `Counter`| O(n)      | O(n)      |
