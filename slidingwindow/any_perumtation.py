'''Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. 
For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters, it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
u    
m
p
i
r
e'''
#let's try with rolling hash algorithm 
print(" =======first approach ========")
def any_permuate(string,pattern):
    start,curr_value = 0,1
    ord_value_pattern=0
    for alp in pattern:
        ord_value_pattern += (ord(alp)-ord('a'))
    print('ord hhhvalue ',ord_value_pattern)
    for end in range(len(string)):
        ord_value = ord(string[end])-ord('a')
        print('ord value',ord_value)
        curr_value += ord_value
        print('test ',(end-start+1))
        print('start is',start)
        if (end-start+1)==len(pattern):
            if ord_value_pattern==curr_value:
                return True 
            else:
                curr_value -= ord(string[start])
                start+=1
    return False 
print(any_permuate("oidbcaf","abc"))

print("====sliding window approach===")
from collections import Counter
def any_permuate1(s,p):
    start,matched =0,0
    freq=Counter(p)
    for end in range(len(s)):
        char = s[end]
        if char in freq:
            freq[char]-=1
            if freq[char]==0:
                matched += 1
        # condition when 
        if matched == len(freq):
            return True 
        #shrink window 
        if end >= len(p)-1:
            left_char = s[start]
            start += 1
            if left_char in freq:
                if freq[left_char]==0:
                    matched -= 1
                freq[left_char]+=1
    return False 
print(any_permuate1("oidbcaf","abce"))#false 
print(any_permuate1('abied','ab'))#true 
    


    
