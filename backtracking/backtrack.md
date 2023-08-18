```
'''
backtracking 
def dfs( parameter ):

	if stop condtion or base case:
		# base case:
		update result
	    return
	
	else:
		# general cases:
		for all possible next moves:
		    select one next move
			dfs( paramter with selected next move )
			undo the selection # back tracking 
	
		return
```
```
  ** pseudo algorithm **
  explore choices : 
   -> if there are non more choices to make:STOP
  -> else for eeach availavle choice C : 
    • choose c 
    •explore the remaining choices ( recursive call)
    •un-chooses c if necessay back track 
```
```
append
recursion function call 
pop
```