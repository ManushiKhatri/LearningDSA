'''
3. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Examples
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

'''
def generate_parenthesis(n):
  final_output = []
  def helper(left_paren,right_paren,pairs):
    print("left_paren and right paren",(left_paren,right_paren))
    print('pairs is',pairs)
    if right_paren < left_paren:
      return 
    if left_paren==0 and right_paren==0:
      final_output.append(''.join(pairs))
    if left_paren > 0:
      #make choice 
      pairs.append('(')
      helper(left_paren-1,right_paren,pairs)
      pairs.pop() # backtrack 
    if right_paren > 0:
      pairs.append(')')
      helper(left_paren,right_paren-1,pairs)
      pairs.pop()
  helper(n,n,[])
  return final_output
print(generate_parenthesis(2))
print(generate_parenthesis(1))
print(generate_parenthesis(2))