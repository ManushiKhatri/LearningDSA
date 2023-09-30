
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.val == None:
        rootNode.val = nodeValue
    elif nodeValue <= rootNode.val:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"

    def inorderTraversal(self,root):
        if not root:
            return None 
        self.inorderTraversal(root.left)
        print(root.val)
        self.inorderTraversal(root.right)
    

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
newBST.inorderTraversal(self,newBST)

