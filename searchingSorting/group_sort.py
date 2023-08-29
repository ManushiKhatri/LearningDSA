'''
Group Sort
Given an array whose elements are only the numbers 0, 1, and 2 (repeated any number of times), sort the array. This must be done in place. 
Try to do it in one pass of the array using only constant space.

Examples:

[2, 1, 1, 0, 2, 1] -> [0, 1, 1, 1, 2, 2]      
[1, 1, 2, 0, 2] -> [0, 1, 1, 2, 2]

You can try this iteratively or recursively. If recursively, feel free to write a helper method.

Note: The implications of this are very cool! Imagine objects colored red, green, and blue. 
We can label those colors 0, 1, and 2, respectively, and now we can sort them in place in linear time! Linear-time sorts do exist, they just have constraints, such as this case of having only 3 values.


'''
# may be counting sort algorithm ??
def group_sort(nums):
    bucket = [0]*3 # since we will only have 3 numbers
    for num in nums:
        bucket[num]+=1
    final_result = [] # len(nums) -> no constant space 
    for i in range(len(bucket)):
        i_count = bucket[i]
        for count in range(i_count):
            final_result += [i]
    return final_result 

print(group_sort([2, 1, 1, 0, 2, 1]))

print("======")
print("in place sorting ")
def group_sort1(nums):
    red , blue = 0, len(nums)-1
    green =0
    while green <= blue:  # O(blue)==O(n)
        if nums[green] == 0:  # swapping red / green
            nums[red], nums[green] = nums[green], nums[red]
            red += 1
            green += 1
        elif nums[green] == 2:  # swapping green and blue
            nums[green], nums[blue] = nums[blue], nums[green]
            blue -= 1
        else:
            green += 1
    return nums
print(group_sort1([2, 1, 1, 0, 2, 1]))