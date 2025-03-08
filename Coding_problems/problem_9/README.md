# Word Ladder Problem

## Problem Statement
Given two words (beginWord and endWord), and a dictionary of words (wordList), find the shortest transformation sequence from beginWord to endWord such that:

- Only *one letter* can be changed at a time.
- Each transformed word must exist in the *wordList*.
- beginWord is *not considered a transformed word*.

If no valid transformation exists, return 0.

### *Example*
#### *Input*
```python
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
```
Output

5

Explanation

hit → hot → dot → dog → cog


---

Optimized Approach: Bidirectional BFS

Instead of searching from just one direction (beginWord → endWord), we search from both ends simultaneously. This significantly reduces the number of words processed, making the algorithm more efficient.

Algorithm Steps

1. Use Two Sets (beginSet, endSet)

Start with beginWord in beginSet, and endWord in endSet.

Always expand the smaller set first to optimize performance.



2. Use a wordSet for Quick Lookups

Converts wordList into a set for O(1) lookup.

Removes words as they are visited to prevent redundant searches.



3. Bidirectional BFS Traversal

Generate new words by changing one letter at a time.

If a word from beginSet matches a word in endSet, we have found the shortest transformation.

Otherwise, continue expanding the search from both ends.





---

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(wordLadder(beginWord, endWord, wordList))  # Output: 5


---

Complexity Analysis

M = Length of each word.

N = Number of words in wordList.

Bidirectional BFS significantly reduces the search space, making it much faster in practice.



---

Why is This Efficient?

✅ Reduces Search Depth: Instead of traversing an entire graph, it only explores half the depth.
✅ Minimizes Memory Usage: Uses fewer nodes at a time, reducing space complexity.
✅ Optimized for Large Word Lists: Works better for large dictionaries compared to normal BFS.


---

Example Execution

Initial State:

beginSet = {"hit"}
endSet = {"cog"}
wordSet = {"hot", "dot", "dog", "lot", "log", "cog"}

Step-by-Step Execution

1. hit → hot
beginSet = {"hot"}


2. hot → dot, lot
beginSet = {"dot", "lot"}


3. dot → dog, lot → log
beginSet = {"dog", "log"}


4. dog → cog (Match with endSet! Transformation found!)



Output: 5 steps. ✅


---

Conclusion

Using Bidirectional BFS, we significantly improve performance compared to a traditional BFS approach.
This method ensures optimal efficiency and scales well for large inputs.

🔹 Bidirectional BFS = Faster Word Ladder Search! 🚀

---

### *How to Use This File*
1. Create a new repository on *GitHub*.
2. Add this *README.md* file to the repository.
3. Include the Python script in a separate file, e.g., *word_ladder.py*.
4. Push the files to GitHub.

This makes it a well-documented solution ready for sharing! 🚀 Let me know if you need further refinements!
