def max_profit(prices):
  if not prices:
    return 0
  n = len(prices)
  min_price = 0
  left_profit = [0]*n

  for i in range(1,n):
    min_price = min(min_price , price[i])
    left_profit[i] = max(left_profit[i-1] , price[i] - min_price)










maxprofit([3,3,5,0,0,3,1,4]) 
