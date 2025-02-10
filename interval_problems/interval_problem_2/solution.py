def solution(interval):
  interval.sort(key = lambda x:x[1])
  output = 0
  previous_end = float('-inf')
  for start , end in interval :
    if start >= previous_end:
      previous_end = end
    else:
      output += 1
  return output


interval = [[1,2],[2,3],[3,4],[1,3]]
print(solution(interval))
