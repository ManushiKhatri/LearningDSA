'''
Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.

Example

For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].
Here are the number of times each digit appears in the array:

0 -> 0
1 -> 1
2 -> 2
3 -> 2
4 -> 1
5 -> 2
6 -> 0
7 -> 1
8 -> 1

The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

Input/Output
[execution time limit] 0.5 seconds (cpp)
[input] array.integer a
An array of positive integers.

Guaranteed constraints:
1 ≤ a.length ≤ 103,
1 ≤ a[i] < 100.

[output] array.integer
The array of most frequently occurring digits, sorted in ascending order.

'''
def frequently_used_number(arr):
    #edge case 
    if not arr:
        return []
    number_count = [0]*10
    max_count = 0
    for number in arr:
        number = str(number)
        for num in number:
            ind = ord(num)-ord('0') 
            number_count[ind]+=1
            if number_count[ind] > max_count:
                max_count = number_count[ind]
    final_answer = []
    for index in range(10):
        if number_count[index]==max_count:
            final_answer.append(index)
    return final_answer
            
print(frequently_used_number([25, 2, 3, 57, 38, 41])) # [2,3,5]
print(frequently_used_number([25555, 22225, 3, 57, 38, 41])) # [5]
print(frequently_used_number([])) # [2,3,5]