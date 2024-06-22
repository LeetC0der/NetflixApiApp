class TreeNode:
    def __init__(self, name, data):
        self.name = name 
        self.details = data
        self.right = None 
        self.left = None

class DirectorTree:
    def __init__(self):
        self.root = None 
    
    def insert(self, name, data):
        if not self.root:
            self.root = TreeNode(name, data)
        else:
            return self.r_insert(self.root, name, data)
    def r_insert(self,node, name, data):
        if name == node.name:
            node.details.append(data)
            return
        if name > node.name:
            if not node.right:
                node.right = TreeNode(name, data)
                return 
            else:
                self.r_insert(node.right, name, data)
        if name < node.name:
            if not node.left:
                node.left = TreeNode(name, data)
                return 
            else:
                self.r_insert(node.left, name, data)

def printTree(node):
    if node:
        print(node.name, node.data)
        if node.left:
            printTree(node.left)
        if node.right:
            printTree(node.right)