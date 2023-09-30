
'''
You are given a string of digits panel and an array of strings codes . Each string in the codes array consists of digits only and represents a code in the following format: "<index><pattern>", where both index and pattern should consist of at least one digit. Since there are several ways to split the code, let's consider them all in ascending order of index length and call them
split-cases. For instance, for the code = "1324", the split-cases are:
• split-case 1: index = "¡" and pattern = "324.
• split-case 2: index = "13" and pattern = "24"
•split-case 3: index = "132" and pattern = "4"
For each code in codes and for every split-case of this code, check whether a string pattern is present at the index position in the panel string. Return a string array consisting of results of these checks, where each element is either pattern, if this pattern is present in panel, or otherwise "not found"
Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than (codes. length × max (codes)
panel. length) will fit within the execution time limit.
@ app.codesignal.com
Question 2 of 4 v
main.py3
1 def solution
2
3
Example
• For panel = "2311453915" and codes = ["0211", "639"] , the output
should be solution (panel, codes) = ["not found", "11", "not
found", "39", "not found"]


'''


def solution(panel, codes):
    results = []
    for code in codes:
        for i in range(1, len(code)):
            index, pattern = int(code[:i]), code[i:]
            if index < len(panel) and panel[index:index+len(pattern)] == pattern:
                results.append(pattern)
            else:
                results.append("not found")

    return results

# Example usage:
panel = "2311453915"
codes = ["211", "639"]
output = solution(panel, codes)
print(output)  # Expected Output: ["not found", "11", "not found", "39", "not found"]







