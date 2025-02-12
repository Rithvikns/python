# The problem statement

solve this Find Right Interval

You are given an array of intervals, where intervals[i] = [start[i], end[i]) and each start[i] is unique.

The right interval for an interval i is an interval j such that start[j] >= end[i] and start[j] is minimized.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put 1 at index i.

Example 1:

Input: intervals = [[1,2]]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:

Input: intervals = [[3,4],[2,3],[1,2]]

Output: [-1,0,1]

## Algorithm

Sorting: We store the start points along with their original indices and sort them.
Binary Search: For each interval, we use bisect_left to find the smallest start point that is ≥ the interval's end.
Result Construction: If a valid right interval exists, we append its index; otherwise, we append -1.

## Solution

### Step 1 

We iterate over intervals, storing the start values and their original indices as tuples (start, index).
The list is then sorted based on the start values.
This allows us to perform binary search efficiently in the next step.
Example for input [[3,4],[2,3],[1,2]]:
Original intervals (indexed): [(3,4), (2,3), (1,2)]
Sorted by start value: [(1,2,2), (2,3,1), (3,4,0)]
starts = [1, 2, 3] (just the start values)

### Step 2

We iterate through each original interval [start, end].
We use bisect_left(starts, end), which finds the first index in starts where end could be inserted while maintaining order.
If idx is within bounds, it means we found a valid right interval.

### Step 3

If idx is within the list's length, we retrieve the original index from sorted_intervals[idx].
Otherwise, we append -1 (no right interval exists).
Finally, we return the result list.



