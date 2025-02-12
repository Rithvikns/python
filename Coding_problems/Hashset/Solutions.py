def unique_pairs(inp_arr):
    inp_arr.sort()
    seen = set()  # Store unique elements
    pairs = set()  # Store unique pairs

    for num in inp_arr:
        print(seen , pairs)
        compliment = -num
        if compliment in seen:
            pairs.add((min(compliment , num),max(num , compliment)))
        seen.add(num)

    return sorted([list(pair) for pair in pairs ])

# Example usage
arr = [-1, 0, 1, 2, -1, -4, 4]
print(unique_pairs(arr))  # Output: [(-1, 1), (-4, 4)]
