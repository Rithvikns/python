import re


def check_float(num):
  pattern = (r'^[+-]?\d*\.\d+$')
  if re.match(pattern,num):
    try:
      float(num)
      return True
    except ValueError:
      return False
  return False

  
T = int(input())

for _ in range(T):
  print(check_float(input()))
