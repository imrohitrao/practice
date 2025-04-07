import time

def cache(func):
    cacher = {}
    def wrappers(*args):
        if args in cacher:
            return cacher[args]
        result = func(*args)       
        cacher[args] = result
        return result
    return wrappers

@cache
def long_running_task(a,b):
    time.sleep(2)
    return a + b

print(long_running_task(6,3))
print(long_running_task(0,9))
print(long_running_task(0,9))



# The reason the `cacher` dictionary stores a **tuple of arguments as a key** lies in how Python functions and dictionaries work. Let me explain the mechanics of this behavior in detail, especially focusing on **why the tuple of arguments is stored as a key in the `cacher` dictionary**.

# ---

# ### **Key Points for the Fourth Line (`cacher[args] = result`)**

# #### **Why Are the Arguments Stored as Keys in `cacher`?**
# 1. **`args` is a Tuple**:
#    - The `*args` syntax in Python collects all positional arguments passed to a function into a tuple.
#    - For example:
#      - If you call `long_running_task(2, 3)`, then `args` becomes `(2, 3)`.
#      - If you call `long_running_task(7, 3)`, then `args` becomes `(7, 3)`.

# 2. **Dictionaries Use Keys to Store and Retrieve Values**:
#    - The `cacher` dictionary uses the tuple `args` as a key to store the corresponding result.
#    - This works because tuples are **hashable** in Python, meaning they can be used as keys in a dictionary. A hashable object has a fixed hash value throughout its lifetime and is immutable.

# 3. **Why Tuples and Not Lists?**
#    - Lists in Python are mutable and therefore not hashable. If `args` were a list, Python would raise a `TypeError` because dictionaries require hashable keys.
#    - Since `args` is a tuple (collected by `*args`), it is immutable and can be used as a dictionary key.

# #### **How the Key-Value Pair is Created in `cacher`?**
# - **Code:**
#   ```python
#   cacher[args] = result
#   ```
# - **Explanation**:
#   - Here, `args` (e.g., `(2, 3)`) is used as the key.
#   - The `result` (the return value of the original function `func(*args)`) is stored as the corresponding value.
#   - This creates a key-value pair in the `cacher` dictionary.

# - **Example**:
#   - If `long_running_task(2, 3)` computes `5`, the `cacher` dictionary after this line will look like:
#     ```python
#     cacher = {
#         (2, 3): 5
#     }
#     ```

# 4. **What Happens During Subsequent Calls?**
#    - If you call `long_running_task(2, 3)` again:
#      - The decorator checks if the tuple `(2, 3)` exists as a key in `cacher` using `if args in cacher`.
#      - Since `(2, 3)` is already stored in `cacher`, the cached value `5` is fetched and returned directly, skipping the function execution.

# ---

# ### **Why Does This Happen Automatically?**

# The behavior arises from the use of a dictionary (`cacher`) to store computed results. Dictionaries map **keys** to **values**, and since `args` is always a tuple when collected via `*args`, it becomes a natural fit as a key in the dictionary.

# #### **How Python Implements It Internally:**
# - When you assign `cacher[args] = result`:
#   - Python calculates the **hash value** of the tuple `args` (e.g., `(2, 3)`).
#   - The hash value is used to locate the storage bucket in the dictionary where the key-value pair should be placed.
#   - The tuple itself (not its hash) is stored as the key, along with its associated value.

# ---

# ### **Example to Understand How Keys Are Stored in `cacher`**
# Let’s see a step-by-step illustration:

# 1. **Initial Call**:
#    - Function call: `long_running_task(2, 3)`
#    - `args = (2, 3)`
#    - Result of the function: `5`
#    - `cacher[(2, 3)] = 5`

#    **Dictionary State**:
#    ```python
#    cacher = {
#        (2, 3): 5
#    }
#    ```

# 2. **Subsequent Call**:
#    - Function call: `long_running_task(2, 3)`
#    - `args = (2, 3)`
#    - `if args in cacher:` evaluates to `True` because `(2, 3)` is already stored.
#    - Cached value `5` is fetched directly.

# ---

# ### **Conclusion**
# The tuple of arguments is stored as a key in the `cacher` dictionary because:
# 1. `*args` automatically creates a tuple of the function’s arguments.
# 2. Tuples are immutable and hashable, making them valid dictionary keys.
# 3. The assignment `cacher[args] = result` explicitly associates the tuple of arguments with the computed result in the dictionary.

# This mechanism ensures that the cache works efficiently and uniquely identifies each set of function arguments.