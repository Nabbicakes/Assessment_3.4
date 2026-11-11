
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create Binary Tree
def create_tree():
    N = Node("N")
    A = Node("A")
    L = Node("L")
    B = Node("B")
    E = Node("E")

    N.left = A
    N.right = L
    A.left = B
    A.right = E

    return N


# BFS - Visit level by level
def bfs(root):
    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


# DFS - Pre-order
def dfs(root):
    if root is None:
        return []

    result = [root.value]
    result += dfs(root.left)
    result += dfs(root.right)

    return result


# Main Program
root = create_tree()

print("BINARY TREE USING NABLE")
print("BFS:", " -> ".join(bfs(root)))
print("DFS:", " -> ".join(dfs(root)))
