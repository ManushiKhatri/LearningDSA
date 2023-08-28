'''
Given a positive integer num, write a function which returns True if num is a
perfect square else False.
Note: Do not use any built-in library function such as sqrt.
Example 1:
Input: 16
Output: true
Example 2:
Input: 14
Output: false

'''
def find_sqrt(n:int):
    if n==1:
        return True 
    if n < 1:
        return False 
    
    left , right = 0 , n//2
    while left <= right:
        mid = left + (right-left)//2
        sqr = mid * mid 
        if sqr == n:
            return True 
        elif sqr < n:
            left +=1 
        else:
            right -=1 
    return False 
print(find_sqrt(1))
        

    