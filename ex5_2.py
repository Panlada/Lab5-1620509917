class Node:
  
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None 
  
  
# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print ("Node: ",root.key,"is child" ,end=" ")
        if root.parent == None:
            print("Parent : NULL")
        else:
            print("Parent  is : ", root.parent.key)
        inorder(root.right)
        
        
  
  
# A utility function to insert a
# new node with given key in BST
def insert(node, key):
  
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)
  
    # Otherwise recur down the tree
    if key < node.key:
        lchild = insert(node.left, key)
        node.left = lchild
        # Set parent of root of left subtree
        lchild.parent = node
    elif key > node.key:
        rchild = insert(node.right, key)
        node.right = rchild
        # Set parent of root of right subtree
        rchild.parent = node
  
    # return the (unchanged) node pointer
    return node
  
# Given a non-empty binary 
# search tree, return the node
# with minimum key value 
# found in that tree. Note that the
# entire tree does not need to be searched
  
  
def minValueNode(node):
    current = node
  
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
  
    return current
  
# Given a binary search tree and a key, this function
# delete the key and returns the new root
  
  
def deleteNode(root, key):
  
    # Base Case
    if root is None:
        return root
  
    # If the key to be deleted 
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
  
    # If the kye to be delete 
    # is greater than the root's key
    # then it lies in right subtree
    elif key > root.key:
        root.right = deleteNode(root.right, key)
  
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
  
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
  
        elif root.right is None:
            temp = root.left
            root = None
            return temp
  
        # Node with two children: 
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
  
        # Copy the inorder successor's 
        # content to this node
        root.key = temp.key
  
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
  
    return root
def maxDepth(node):
    if node is None:
        return 0
 
    else:
 
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

def printLeafNodes(root: Node) -> None:
 
    # If node is null, return
    if (not root):
        return
 
    # If node is leaf node,
    # print its data
    if (not root.left and
        not root.right):
        print("leaf",root.key,
              end = " ")
        return
 
    # If left child exists,
    # check for leaf recursively
    if root.left:
        printLeafNodes(root.left)
 
    # If right child exists,
    # check for leaf recursively
    if root.right:
        printLeafNodes(root.right)
def CheckIfNodesAreSiblings(root, data_one,
                                  data_two):
     
    if (root == None):
        return False
 
    # Compare the two given nodes with
    # the childrens of current node
    ans = False
     
    if (root.left != None and root.right != None):
        left = root.left.key
        right = root.right.key
         
        if (left == data_one and right == data_two):
            return True
        elif (left == data_two and right == data_one):
            return True
 
    # Check for left subtree
    if (root.left != None):
        ans = ans or CheckIfNodesAreSiblings(root.left,
                                       data_one,
                                       data_two)
                                        
    # Check for right subtree
    if (root.right != None):
        ans = ans or CheckIfNodesAreSiblings(root.right,
                                       data_one,
                                       data_two)
         
    return ans   

# Use the insert method to add nodes
root = Node(50)
root = insert(root,25)
root = insert(root,75)
root = insert(root,30)
root = insert(root,60)
root = insert(root,40)

""" print ("Inorder traversal of the given tree")
inorder(root)
print("\n Delete Node 30")
root = deleteNode(root,30)
print ("Inorder traversal of the given tree")
inorder(root)
print("\n Delete Node 75")
root = deleteNode(root,75)
print("Inorder traversal of the given tree")
inorder(root)
print("\n Delete Node 40")
root = deleteNode(root,40)
print("Inorder traversal of the given tree \n")
inorder(root) """

############
inorder(root)
print("Height of tree is:",(maxDepth(root)))
printLeafNodes(root)

data_one = 60

data_two = 40

if (CheckIfNodesAreSiblings(root,data_one,data_two)):
    print("\n YES")
else:
    print("\n NO")