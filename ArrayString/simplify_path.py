'''
Implement a program to accept an input file containing file paths separated by slashes and lines and build a directory system representing the data paths.

Given a list of strings that represent files, output the Directory structure
represented by these files.

Example:
Input files =  [
  “/app/components/header”,
  “/app/services”,
  “/app/tests/components/header”,
  “/images/image.png”,
  "/tsconfig.json",
  "/index.html",
];

Output:
-- app
  -- components
		-- header
	-- services
	-- tests
		-- components
			-- header
-- images
  -- image.png
-- tsconfig.json
-- index.html

'''

from collections import OrderedDict
class TrieNode:
    def __init__(self):
        self.children = OrderedDict()
        self.end_of_dir = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_dir(self, words, order):
        current = self.root
        for word in words:
            if word not in current.children:
                current.children[word] = (TrieNode(), order)
            current, _ = current.children[word]

        current.end_of_dir = True


def print_paths_trie(trie, indent=""):
    for key, (child, _) in trie.children.items():
        print(indent + key)
        print_paths_trie(child, indent + "-")


def create_trie(paths):
    trie = Trie()
    for order, path in enumerate(paths):
        if not path:
            continue
        if path[0] == '/':
            path = path[1:]
        portions = path.split('/')
        trie.insert_dir(portions, order)

    return trie


paths = ['/a/c/ac', 'a/b/ab', 'b/c/bc', 'a/c/ac2']
trie = create_trie(paths)
print_paths_trie(trie.root)
files = [
    "/app/components/header",
    "/app/services",
    "/app/tests/components/header",
    "/images/image.png",
    "/tsconfig.json",
    "/index.html",
]
trie = create_trie(files)
print_paths_trie(trie.root)
# expected -c
'''-c
--ac
--ac2
-b
--ab
b
-c
--bc'''

# without Trie 
print()
print("another solution ")




# def construct_map(paths):
    
#     structure = {}
#     for file in paths:
#         components = file.split('/')
#         current_structure = structure
#         for component in components:
#             if component not in current_structure:
#                 current_structure[component] = {}
#             current_structure = current_structure[component]

#     return structure
def construct_map(paths):
    my_map = {}  # Initialize an empty dictionary to represent the directory structure
    map_ptr = my_map  # Create a pointer to navigate through the dictionary

    for path in paths:
        # Split the path into individual directory components
        path_items = path.split('/')
        for i in path_items:
            if i not in map_ptr.keys():
                # Create a new dictionary for the current directory component
                map_ptr[i] = {}
            # Move the pointer to the next level in the directory structure
            map_ptr = map_ptr[i]
        map_ptr = my_map  # Reset the pointer for the next path

    return my_map

print(construct_map(['a/c/ac', 'a/b/ab', 'b/c/bc', 'a/c/ac2']))
            
            

def print_map(my_map):
    for key in my_map.keys():
        print_recursive(my_map.get(key), key, 0)


def print_recursive(my_map: dict, key: str, depth: int):
    # Print the current directory component with indentation based on depth
    print(depth * "-" + key)
    for i in my_map.keys():
        # Recursively print the subdirectories
        print_recursive(my_map.get(i), i, depth + 1)


paths = ['a/c/ac', 'a/b/ab', 'b/c/bc', 'a/c/ac2']

# Construct the directory structure map and print it
print_map(construct_map(paths))






        

