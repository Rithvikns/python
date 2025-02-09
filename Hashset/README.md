# HashSet

## Definition:

A HashSet is a collection of unique elements. It does not allow duplicates and offers O(1) average time complexity for insertions, deletions, and lookups.

### Key Characteristics:

Stores only unique elements (No duplicates).
Uses hashing for fast lookups.
collection (No index-based access).
Efficient O(1) operations (on average).

Use Case: When you need fast membership checks and only unique values.

# HashMap

## Definition:

A HashMap is a collection of key-value pairs, where each key is unique and maps to a specific value.

### Key Characteristics:
Stores data as key-value pairs.
Keys must be unique (values can be duplicate).
Uses hashing for fast lookups, insertions, and deletions (O(1) on average).
Unordered collection (No fixed order of elements).

Use Case: When you need fast lookups and associative data storage (key-value mapping).

## Difference Between HashSet and HashMap

| Feature      | HashSet (`set`) | HashMap (`dict`) |
|-------------|---------------|----------------|
| **Stores**  | Unique elements | Key-Value pairs |
| **Duplicates Allowed?** | ❌ No (only unique values) | ✅ Keys must be unique, but values can repeat |
| **Lookup Time Complexity** | O(1) on average | O(1) on average |
| **Order of Elements** | Unordered | Unordered (but insertion order preserved in Python 3.7+) |
| **Operations** | Add, remove, check membership | Insert, update, delete, get value by key |
| **Implementation** | Uses a Hash Table | Uses a Hash Table |
