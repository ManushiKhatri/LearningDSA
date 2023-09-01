'''Given a string str, two characters X and Y. The task is to find the length of the longest substring that starts with X and ends with Y. It is given that there always exists a substring that starts with X and ends with Y. 
Examples: 
 

Input: str = “QWERTYASDFZXCV”, X = ‘A’, Y = ‘Z’ 
Output: 5 
Explanation: 
The largest substring which start with ‘A’ and end with ‘Z’ = “ASDFZ”. 
Size of the substring = 5.
Input: str = “ZABCZ”, X = ‘Z’, Y = ‘Z’ 
Output: 3 
Explanation: 
The largest substring which start with ‘Z’ and end with ‘Z’ = “ZABCZ”. 
Size of the substring = 5. 

'''
print('naive approach')
def longest_substring(s,first,last):
    start,max_length = 0,0
    for end in range(len(s)):
        right_char = s[end]
        print('right char is',right_char)
        if right_char==first:
            start=end+1
            while start < len(s):
                print('sstart',s[start])
                if s[start]==last:
                    max_length=max(start-end+1,max_length)
                    start=end+1
                    break
                start+=1
    return max_length
print(longest_substring('QWERTYASDFZXCV','A','Z'))#5
print(longest_substring('ZAAABCZZ','A','Z')) #7
print(longest_substring("HASFJGHOGAKZZFEGA",'A','Z'))#12
            
print("==another optimize approach==")
print()
def longest_substring1(s,first,last):
    start,end =0,len(s)-1
    while start < len(s): #O(n)-> worst case 
        if s[start]==first:
            break 
        start+=1
    print('start is',start)
    while end > 0: #-> O(n)-> worst case 
        if s[end]==last:
            break 
        end-=1
    print('end is',end)
    max_length=(end-start+1)
    return max_length
print(longest_substring1('QWERTYASDFZXCV','A','Z'))#5
print(longest_substring1('ZAAABCZZ','A','Z')) #
print(longest_substring1("HASFJGHOGAKZZFEGA",'H','A'))#12