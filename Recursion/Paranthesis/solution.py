def generate_paranthesis(n):
  def recursion(n,diff,current_list):
    if n == 0:
      output.append("".join(current_list[:]))
      return 
    if diff < 0 or diff > n:
      return
    
