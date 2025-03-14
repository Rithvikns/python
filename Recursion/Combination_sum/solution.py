from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, combination, current_sum):
            if current_sum == target:
                result.append(list(combination))
                return
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, current_sum + candidates[i])
                combination.pop()  # Backtrack
        
        backtrack(0, [], 0)
        return result
