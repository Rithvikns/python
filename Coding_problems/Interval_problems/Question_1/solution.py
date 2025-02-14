from bisect import bisect_left

def findRightInterval(intervals):
    # Store the start indices along with their original indices
    sorted_intervals = sorted((start, i) for i, (start, end) in enumerate(intervals))
    starts = [s[0] for s in sorted_intervals]
    
    result = []
    for start, end in intervals:
        # Find the index where end would fit in sorted starts
        idx = bisect_left(starts, end)
        # If idx is within range, get the corresponding original index
        if idx < len(intervals):
            result.append(sorted_intervals[idx][1])
        else:
            result.append(-1)
    
    return result

# Example test cases
print(findRightInterval([[1,2]]))  # Output: [-1]
print(findRightInterval([[3,4],[2,3],[1,2]]))  # Output: [-1, 0, 1]
