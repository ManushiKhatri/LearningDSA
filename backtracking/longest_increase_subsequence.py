'''

## Longest Increasing Subsequence

Given a list `nums`, return a list of the longest increasing subsequence found in the list. For example:

```
[6, 37, 2, 4, 18, 7] -> [2, 4, 7]
```

This is because the numbers 2, 4, and 7 are increasing and appear in that order in the list (though not necessarily immediately consecutively). 
Other increasing subsequences present in the list are [6, 37], [6, 18], [7], and so on.


6 37 2 4 18 7 

include  6 --
exclude 37 --
    


'''
def longest_increasing_subsequence(nums):
    # Base case 
    if not nums:
        return []

    # Helper function 
    def helper(curr_index, current):
        # Base case 
        if curr_index >= len(nums):
            return current
        include = []
        # Check if we can include the current number
        if not current or nums[curr_index] > current[-1]:
            include = helper(curr_index + 1, current + [nums[curr_index]])

        exclude = helper(curr_index + 1, current)

        return include if len(include) > len(exclude) else exclude

    return helper(0, [])

nums = [6, 37, 2, 4, 18, 7]
print(longest_increasing_subsequence(nums))  # Expected output: [2, 4, 7]

nums = [10,9,2,5,3,7,101,18]
print(longest_increasing_subsequence(nums))

    