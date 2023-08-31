'''
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
 '''
def flip_zero(nums,k):
     start,max_length = 0,0
     count = 0
     for end in range(len(nums)):
         
         right_num = nums[end]
         if right_num == 0:
             count += 1
         while count >k:
            left_num = nums[start]
            if left_num==0:
                count -= 1
            start+=1
         max_length = max(max_length,end-start+1)
     return max_length
print(flip_zero([1,1,1,0,0,0,1,1,1,1,0],2)) # 6 
        

            
            
        


