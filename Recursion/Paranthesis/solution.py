def generate_paranthesis(n):
  def recursion(n,diff,current_list):
    if n == 0:
      output.append("".join(current_list[:]))
      return 
    elif diff < 0 or diff > n:
      return
    else:
      current_list.append('(')
      recursion(n-1,diff+1,current_list)
      current_list.pop()
      current_list.append(')')
      recursion(n-1,diff-1,current_list)
      current_list.pop()
  output = []
  recursion(2*n,0,[])
  return output

print(generate_paranthesis(3))
