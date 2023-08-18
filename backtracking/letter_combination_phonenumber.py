'''
##leetcode 17
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

'''
def letter_combination_phone_number(digits):
  number_letter = {'2':['a','b','c'],
                            '3':['d','e','f'],
                            '4':['g','h','i'],
                            '5':['j','k','l'],
                            '6':['m','n','o'],
                            '7':['p','q','r','s'],
                            '8':['t','u','v'],
                            '9':['w','x','y','z']
                           }
  final_output = []
  if len(digits) == 0:
    return []

  def helper(pairs,index):
    #base case -> index track
    if index == len(digits):
      final_output.append(''.join(pairs))
      return
    letters = number_letter[digits[index]]  #
    print("letters is ",letters)
    for i in range(len(letters)):
      print("i is",i)
      current = letters[i]
      pairs.append(current)
      print('pairs is',pairs)
      helper(pairs,index+1)
      pairs.pop()

  helper([],0)

  return final_output
print(letter_combination_phone_number('23'))
print(letter_combination_phone_number(""))