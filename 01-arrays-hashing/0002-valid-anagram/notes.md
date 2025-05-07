# Notes on sorted() vs list.sort()

## ✅ Key Difference

| Expression      | Meaning                                      | Result                   |
|------------------|-----------------------------------------------|---------------------------|
| `sorted(list)`   | Passes the list into a function and returns a **new sorted list** | New list (product)        |
| `list.sort()`    | Refers to the **action of sorting in-place** | The original list is modified (product), but the `.sort()` call itself returns nothing |

- `sorted(list)` is like getting a new product from a factory.
- `list.sort()` is the factory process itself — it modifies the original list, and **returns nothing**.
- Trying to assign the result of `list.sort()` will give you `None`.

## ✅ Correct usage

```python
# Use sort() when you want to modify the original list
lst = [3, 1, 2]
lst.sort()
print(lst)  # [1, 2, 3]

# Use sorted() when you want to keep the original list unchanged
lst = [3, 1, 2]
new_lst = sorted(lst)
print(new_lst)  # [1, 2, 3]
print(lst)      # [3, 1, 2]

