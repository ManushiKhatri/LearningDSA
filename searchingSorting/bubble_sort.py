'''
Bubble Sort Algorithm

-> also referred as sinking sort 
-> repeatedly compare each pair of adjacent and swap them if 
they are in wrong order 

'''
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            print(i,j)
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums 

nums=[9,3,2,4,5,1,6,2,3]
print(bubble_sort(nums))

# time complexity - TC=O(n^2)
#space complexity - SC=O(1)