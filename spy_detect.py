'''
As a spy, you've been tasked with recovering some stolen artwork. You've entered the room containing the artwork, and have detected some security systems in place. 

The room is represented as a matrix, where the spy "S" is in the top left (0,0), open locations are "-", spaces with the security system are "D" and the artwork is "A".

Example:
room = [
    ['S', '-', '-', '-', 'D'],
    ['-', 'D', 'D', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['D', 'D', '-', '-', '-'],
    ['-', 'D', '-', 'A', '-'],
    ['-', 'D', '-', '-', '-'],
]
You've been provided with a series of instructions. These are provided as a string of directions to move, using the characters N (north/up), S (south/down), E (east/right), W (west/left).

Example: "NNSSWW" = North, North, South, South, West, West.

Given a room and a list of instructions. Return whether you reach the artwork without getting detected. You are detected if you hit the security system or the walls of the room before reaching the artwork.

All Test Cases:
detected(room, "SSEEESS")        => True (got the artwork)
detected(room, "ESSSSEE")        => False (Got detected)
detected(room, "EEENSSSSS")      => False (Hit the wall)
detected(room, "EEESEESSSWW")    => False (Hit the wall)
detected(room, "EEESESSSSWNNNN") => True (got the artwork)
detected(room, "EEESSS")         => False (did not reach the artwork)
detected(room, "NEEESEESSSWW")   => False (Hit the wall)
detected(room, "SWWSSS")         => False (Hit the wall)
detected(room, "SSEEESSWW")      => True (got the artwork)

'''
def detected(room, s):
    #edge case 
    directions ={'S':(1,0),'N':(-1,0),'E':(0,1),"W":(0,-1)}
    if not room:
        return False
    #checkbounds 
    def inbounds(room,r,c):
        return r >= 0 and r < len(room) and c >=0 and c <len(room[r])
    #depth first search 
    def dfs(r,c,index):
        #base case
        # print(f' string and row / col ', {room[r][c]}, (r,c))
        #1.check bound first 
        if not inbounds(room,r,c) or room[r][c]=='D':
            return False 
        #2. check if we hit the target 
        if room[r][c]=='A':
            return True 
        #3.check if wereach the end 

        if index==len(s):
            return False 
        #process all possible directions 
        if s[index] in directions:
            row,col = directions[s[index]]
            new_r = row + r
            new_c = col + c
            # print(new_r,new_c)
            return dfs(new_r,new_c,index+1)
        return False 
    if dfs(0,0,0):
        return True 
    return False

room = [
    ['s', '-', '-', '-', 'D'],
    ['-', 'D', 'D', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['D', 'D', '-', '-', '-'],
    ['-', 'D', '-', 'A', '-'],
    ['-', 'D', '-', '-', '-'],
]
    
print(detected(room, "SSEEESS")) # True 
print(detected(room, "SWWSSS")) # false
print(detected(room, "ESSSSEE"))      # => False (Got detected)
print(detected(room, "EEENSSSSS"))      #=> False (Hit the wall)
print(detected(room, "EEESEESSSWW"))   # => False (Hit the wall)
print(detected(room, "EEESESSSSWNNNN"))# => True (got the artwork)
print(detected(room, "EEESSS"))        #=> False (did not reach the artwork)
print(detected(room, "NEEESEESSSWW"))  # => False (Hit the wall)
print(detected(room, "SWWSSS"))         #=> False (Hit the wall)
print(detected(room, "SSEEESSWW"))    # => True (got the artwork)

#time complexity = O(n*m) in the worst case 
# space complexity = O(n*m) in the worst case 