'''
Insertion Sort Algorithm 

Notes :
• divide the array into two part 
• take first element from unsorted array and find its correct position 
in sorted array
• repeat until unsorted array is empty 

'''
def insertion_sort(nums):
    for i in range(1,len(nums)): # ---> O(n)
        curr = nums[i]           # ---> O(1)
        j = i-1
        while j >= 0 and curr < nums[j]: #-->O(n)
            nums[j+1]= nums[j]
            j -=1 
        nums[j+1]=curr
    return nums 
nums= [9,5,3,2,1,23]
print(insertion_sort(nums))

'''
Time Complexity : 
since we have two iterations: one is nested loop of other 
TC = O(n^2)
SC = O(1) since it's a in place 


'''