# Sliding Window Algorithm
The Sliding Window Algorithm is a technique used to efficiently process contiguous subarrays or subsequences in an array or string. Instead of recomputing results from scratch for each window, the algorithm maintains a window and slides it across the input, updating results incrementally.

## Types of Sliding Windows:
Fixed-size window
The window always contains k elements and slides one step at a time.
Example: Finding the maximum in every k-size subarray.
Variable-size window
The window size expands or shrinks dynamically based on a condition.
Example: Finding the longest substring without repeating characters.
How Sliding Window Works (Fixed-Size Example)
Consider an array and a window size k:

## Applications of Sliding Window Algorithm
1. Maximum/Minimum in Subarrays
Problem: Find the maximum in every window of size k in an array.
Example: Stock price monitoring.
2. Longest Substring Without Repeating Characters
Problem: Find the longest substring in a string without repeating characters.
Example: Used in text processing and pattern matching.
Approach: Expand window while characters are unique, shrink when a repeat is found.
3. Smallest Subarray with a Given Sum
Problem: Find the smallest contiguous subarray whose sum ≥ target.
Example: Financial analytics (minimum days required to reach a profit goal).
Approach: Expand window until sum ≥ target, shrink to minimize size.
4. Count Distinct Elements in Every Window of Size k
Problem: Count distinct numbers in each window.
Example: Data compression and database query optimization.
5. DNA Sequence Analysis
Problem: Find repeating subsequences in genetic strings.
Example: Bioinformatics (detecting mutations, finding regulatory sequences).
6. Network Packet Analysis
Problem: Monitor incoming network packets in a time window.
Example: Intrusion detection, traffic analysis.
7. Video Streaming & Image Processing
Problem: Process a moving window of pixels in a video stream.
Example: Motion detection, object tracking.


## Advantages of Sliding Window Algorithm
Reduces unnecessary computations
Efficient in O(n) time complexity
```console
arr = [1, 3, 5, -2, -6, 9]
k = 3
We compute the maximum for each subarray of size k:
Window [1,3,5] → max = 5
Window [3,5,-2] → max = 5
Window [5,-2,-6] → max = 5
Window [-2,-6,9] → max = 9
Instead of recomputing the max from scratch, we use a deque (double-ended queue) to efficiently track max values, making it run in O(n) time.
```

Optimized for large data sets

This technique is widely used in competitive programming, real-time data processing, and AI/ML applications!

## Deque - Double ended Queue

Deque is a data structure that allows for the efficient addition and removal of elements from both ends. Unlike regular queues, which usually operate on the FIFO (First In, First Out) principle, a Deque supports both FIFO and LIFO (Last In, First Out) operations.
here is the link if you want to know more about deque https://www.geeksforgeeks.org/deque-in-python/

In this problem deque stores the indices of the elements having the maximum number in the window . The deque does not store the elements itself . It always keeps the elements in the descending order of their corresponding value (largest value first).
The front of the deque dq[0] always contains the index of maximum number in the current sliding window. 
Elements that are out of the current window are removed from the front.
Smaller elements (that are useless) are removed from the back.
The first index in dq always represents the largest element in the window.
