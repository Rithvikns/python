def max_profit(prices):
  if not prices:
    return 0
  n = len(prices)
  min_price = 0
  left_profit = [0]*n

  for i in range(1,n):
    min_price = min(min_price , prices[i])
    left_profit[i] = max(left_profit[i-1] , prices[i] - min_price)

  max_price = prices[-1]
  right_profit = [0]*n

  for i in range(n-2,-1,-1):
    max_price = max(max_price , price[i])
    right_profit[i] = max(right_profit[i+1] ,  max_price - prices[i])

  max_profit = 0
  for i in range(n):
    max_profit = max(max_profit , left_profit[i] + right_profit[i])
    return max_profit

maxprofit([3,3,5,0,0,3,1,4]) 
