# Step 1: Create a simple Node class for the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Step 2: Define the traversal functions using simple logic

def preorder(node, result):
    """ Root -> Left -> Right """
    if node is not None:
        result.append(node.value)  # Write/record the parent first[cite: 1]
        preorder(node.left, result)    # Go left[cite: 1]
        preorder(node.right, result)   # Go right[cite: 1]


def inorder(node, result):
    """ Left -> Root -> Right """
    if node is not None:
        inorder(node.left, result)     # Go left first[cite: 1]
        result.append(node.value)  # Write/record the parent in the middle[cite: 1]
        inorder(node.right, result)    # Go right[cite: 1]


def postorder(node, result):
    """ Left -> Right -> Root """
    if node is not None:
        postorder(node.left, result)   # Go left[cite: 1]
        postorder(node.right, result)  # Go right[cite: 1]
        result.append(node.value)  # Write/record the parent last[cite: 1]


# Step 3: Build the tree structure from your notes[cite: 1]

# Root node[cite: 1]
root = Node('M')

# Second level[cite: 1]
root.left = Node('A')
root.right = Node('R')

# Third level under A and R[cite: 1]
root.left.left = Node('K')
root.left.right = Node('N')
root.right.left = Node('A')
root.right.right = Node('B')

# Fourth level under K[cite: 1]
root.left.left.left = Node('L')
root.left.left.right = Node('E')


# Step 4: Run the functions and print the results

pre_list = []
preorder(root, pre_list)
print("Preorder:", ", ".join(pre_list))

in_list = []
inorder(root, in_list)
print("Inorder:", ", ".join(in_list))

post_list = []
postorder(root, post_list)
print("Postorder:", ", ".join(post_list))