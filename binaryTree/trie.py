# making a a trie (prefix tree)
class TrieNode:
     def __init__(self) -> None:
         self.children = {}
         self.end_of_string=False 
         
class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()#initally its blank 
    
    def insert_string(self,word):
        current = self.root
        for char in word:
            print('char is',char)
            print('curren tchilderen ',current.children)
            if char not in current.children:
                current.children[char]=TrieNode() #created node 
            current=current.children[char]
        current.end_of_string=True
        print("Successfully inserted")
        
    def search_string(self,word):
        
        '''
        Case 1: string does not exist
        check first letter of string with the root 
        case 2 : string is a prefix of another string but doesnot exist in a trie 
        case 3: string does exist in a trie 

        '''
        current=self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        if current.end_of_string:
            return True 
        return False 
    
    def starts_with(self,prefix):
        current=self.root
        for char in prefix:
            if char not in current.children:
                return False 
            current=current.children[char]
            print('curr is',current.children)
        return True 
    
def delete_string(root,word,index):
    """
    Case 1 : some other prefix of string is same as the one that we want to delete(Api,apple)
    Case 2 : the string is a prefix of another string(Api,Apis)
    Case 3: Other string is a prefix of the other string
    case 4: not any node depends on the string(k)
    
    """
    ch = word[index]
    if ch in root.children:
        current_node =root.children[ch]
    can_this_be_deleted=False
    if len(current_node.children) > 1:
        delete_string(current_node,word,index+1)
        return False 
    if index==len(word)-1:
        if len(current_node.children)>=1:
            current_node.end_of_string=False 
            return False 
        else:
            root.children.pop(ch)
            return True 
    if current_node.end_of_string == True:
        delete_string(current_node,word,index+1)
        return False
    can_this_be_deleted=delete_string(current_node,word,index+1)
    if can_this_be_deleted:
        root.children.pop(ch)
        return True 
    return False 

    
        
        
    
trie = Trie()
trie.insert_string("app")
trie.insert_string("apply")
print(trie.search_string('ape')) #false 
print(trie.search_string('apply')) #true 
delete_string(trie.root,'app',0)
print(trie.search_string('app')) #false
print(trie.search_string('a')) #false  
print(trie.starts_with('appl')) #true
print(trie.starts_with('jks')) #true