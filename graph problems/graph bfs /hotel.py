'''

You are travelling to Neverland. After a long journey, you decided to take rest in a hotel for a night.

You have the map of Neverland in the form of 2D matrix A with dimensions N x M. 

The rows are numbered from 1 to N, and the columns are numbered from 1 to M.

You can travel from one cell to any adjacent cell. Two cells are considered adjacent if they share a side.

In the map, there are only two digits, 0 and 1, 
where 1 denotes a hotel in that cell, and 0 denotes an empty cell.

You are also given another 2D array B with dimension Q x 2,
 
where each row denotes a co-ordinate (X, Y) on the map (1 - indexed). 
For each coordinate you have to find the distance to the nearest hotel.

Return an array denoting the answer to each coordinate in the array B.



**Problem Constraints**
1 <= N, M <= 103
1 <= Q <= 105
0 <= A[i][j] <= 1
1 <= B[i][0] <= N
1 <= B[i][1] <= M
There is guranteed to be atleast one hotel on the map.


**Input Format**
The first argument is the 2D integer array A.
The second argument is the 2D integer array B.


**Output Format**
Return an integer array denoting the answer to each coordinate in the array B.


**Example Input**
Input 1:
A = [[0, 0],
     [1, 0]]
B = [[1, 1],
     [2, 1],
     [1, 2]]
Input 2:

A = [[1, 0, 0 1]]
B = [[1, 2],
     [1, 3]]


**Example Output**
Output 1:
[1, 0, 2]
Output 2:

[1, 1]


**Example Explanation**
Explanation 1:
(1, 1) is adjacent to a hotel. (2, 1) has a hotel. (1, 2) is two cells away from the hotel on (2, 1).
Explanation 2:

(1, 2) is adjacent to a hotel on (1, 1). (1, 3) is adjacent to a hotel on (1, 4).
'''
