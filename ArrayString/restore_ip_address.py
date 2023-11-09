'''
# leeetcode 93 : https://leetcode.com/problems/restore-ip-addresses/
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

'''
# ip cant have more than 12 integers 
# no leading zeros except for zero itself 
# can be more than 255 
def restore_ip(address):
    final_result = []
    #edge case 
    if len(address) > 12:
        return final_result

    def helper(index, dots, curr_ip):
        #base case
        if dots == 4 and index == len(address):
            final_result.append(curr_ip[:-1])  # Remove the trailing dot and append the valid IP address
            return

        if dots > 4 or index == len(address):
            return
        #iterating over the index 
        for i in range(index, min(index + 3, len(address))): # INCREASING INDEX BY 3 BUT THERE WILL BE THE CASE WHERE WE GO OUT OF BOUND BUT REMAINING CHAR WILL BE LESS THAN 3
            segment = address[index:i + 1]
            if segment == "0" or (segment[0] != '0' and int(segment) <= 255): # checking if the segement is with in the range
                helper(i + 1, dots + 1, curr_ip + segment + '.')

    helper(0, 0, '')
    return final_result

s = "25525511135"
print(restore_ip(s))

