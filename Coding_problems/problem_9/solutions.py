
from collections import deque

def wordLadder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0  # No valid transformation

    beginSet = {beginWord}
    endSet = {endWord}
    wordSet.discard(beginWord)
    wordSet.discard(endWord)
    
    length = 1  # Start at 1 since beginWord itself is counted

    while beginSet and endSet:
        # Always expand the smaller set to keep BFS efficient
        if len(beginSet) > len(endSet):
            beginSet, endSet = endSet, beginSet  # Swap
        
        nextSet = set()
        for word in beginSet:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    
                    if newWord in endSet:  # If we meet in the middle
                        return length + 1
                    
                    if newWord in wordSet:
                        nextSet.add(newWord)
                        wordSet.remove(newWord)  # Mark as visited
        
        beginSet = nextSet
        length += 1  # Increase transformation step

    return 0  # No valid transformation

# Example usage
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(wordLadder(beginWord, endWord, wordList))  # Output: 5
