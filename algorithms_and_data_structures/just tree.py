# по сути просто ноды, с данными, и массивом из таких же нод, типо детьми, по сути это граф
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        
def bfs(root):
    queue = deque([root])
    result = []
    
    while queue:
        cur = queue.popleft()
        result.append(cur.data)
        for child in cur.children:
            queue.append(child)
    return result

def maxDepth( root) -> int:
        stack = [root]
        depth = 0

        if not root:
            return 0

        while stack:
            size = len(stack)
            while size != 0:
                cur = stack.pop()
                for child in cur.children:
                    stack.append(child)
                size -= 1
            depth += 1
        return depth
    
if __name__ == "__main__":
    root = TreeNode(10)
    child1 = TreeNode(124)
    child2 = TreeNode(25)
    child3 = TreeNode(51)
    child4 = TreeNode(125)
    root.add_child(child1)
    root.add_child(child2)
    child2.add_child(child3)
    child3.add_child(child4)
    print(bfs(root))
    print(maxDepth(root))

    
    
            