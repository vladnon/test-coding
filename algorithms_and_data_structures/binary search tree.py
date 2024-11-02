from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        
    def append(self, data):
        new_node = Node(data)
        
        if not self.root:
            self.root = new_node
        else: 
            cur_node = self.root
            while True:
                if data < cur_node.data:
                    if not cur_node.left:
                        cur_node.left = new_node
                        break
                    else:
                        cur_node = cur_node.left
    
                else:
                    if not cur_node.right:
                        cur_node.right = new_node
                        break
                    
                    else:
                        cur_node = cur_node.right
                    
    def search(self, target):
        cur_node = self.root
        while cur_node:
            if target == cur_node.data:
                return True
            
            elif target < cur_node.data:
                cur_node = cur_node.left
            
            else:
                cur_node = cur_node.right
        return False
    
    def max(self):
        cur_node = self.root
        if self.root:
            while cur_node:
                
                if cur_node.right:
                    cur_node = cur_node.right
                
                else:
                    return cur_node.data
        return None
    
    def min(self):
        cur_node = self.root
        if self.root:
            while cur_node:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    return cur_node
        return None
    
    def left(self, data: int) -> bool:
        cur_node = self.root
        while cur_node:
            if data == cur_node.data:
                if cur_node.left:
                    return True, cur_node.left.data
                else:
                    return "None"
            elif data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False
    
    def right(self, data: int) -> bool:
        cur_node = self.root
        while cur_node:
            if data == cur_node.data:
                if cur_node.right:
                    return True, cur_node.right.data
                else:
                    return "None"
            elif data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False


    # этот метод не правильный, нужно доделать, ну если тебе уже сейчас будет не лень, после удаления, надо циклом, проходиться до конца
    #  ветки если ты в левой ветке, тебе нужно брать правого сына как родителя, как левого ребенка левого, ну и наоборт в правой, но это не точно, потому что я еще не писал, и не думал как это будет.
      
    
    def delete(self, data: int):
        cur_node = self.root
        parent = None
        
        if not self.root:
            return 
        
        while cur_node:
            if cur_node.data == data:
                # ситуация, когда у узла либо одни ребенок либо его нет
                if not cur_node.left:
                    if parent:
                        if parent.left == cur_node:
                            parent.left = cur_node.right
                        else:
                            parent.right = cur_node.right
                         
                    else:
                        self.root = cur_node.right 
                       
                elif not cur_node.right:
                    if parent:
                        if parent.right == cur_node:
                            parent.right = cur_node.left
                        else:
                            parent.left = cur_node.left
                         
                    else:
                        self.root = cur_node.right 
                else:
                    # ситуация, когда у узла два потомка
                    child_parent = cur_node
                    child = cur_node.right
                    while child.left:
                        child_parent = child
                        child = child.left
                    cur_node.data = child.data
                    if child_parent.left == child.right:
                        child_parent = child.right
                    else:
                        child_parent.right = child.right
                        
            parent = cur_node    
            if data < cur_node.data:
                cur_node = cur_node.left

            else:
                cur_node = cur_node.right
        return 
    
    
    def delete(self, data):
        cur_node = self.root
        parent = None
        
        if not self.root:
            return parent
        
        while cur_node:
            if cur_node.data == data:
                if not cur_node.left:
                    if parent:
                        if parent.left == cur_node:
                            parent.left = cur_node.right
                        else:
                            parent.right = cur_node.right
                    else:
                        self.root = cur_node.right
                elif not cur_node.right:
                    if parent:
                        if parent.right == cur_node:
                            parent.left = cur_node.right
                    else:
                        self.root = cur_node.right
                        
                else:
                    child = cur_node.right
                    child_parent = cur_node
                    while child.left:
                        child_parent = child
                        child = child.left
                    cur_node.data = child.data
                    if child_parent.left == child.right:
                        child_parent = child.right
                    else:
                        child_parent.right = child.right
            parent = cur_node
            if data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return
                    
    
    def len(self):
        count = 0
        stack = [self.root]
        
        if not self.root:
            return count
        
        while stack:
            node = stack.pop()
            count += 1
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count

    def pre_order(self):
        stack = [self.root]
        result = []
        
        if not self.root:
            return []
        
        while stack:
            cur_node = stack.pop()
            result.append(cur_node.data)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        return result
    
    def iin_order(self):
        stack = []
        result = []
        cur_node = self.root
        
        if not self.root:
            return []
        
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            result.append(cur_node.data)
            cur_node = cur_node.right
        return result
    
    def left_sum_lists(self):
        total_sum = 0 
        stack = [self.root]

        if not self.root:
            return []
        
        while stack:
            cur_node = stack.pop()
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                child_node = cur_node.left
                if not child_node.right and not child_node.left:
                    total_sum += child_node.data
                stack.append(cur_node.left)
            
        return total_sum
    

    def findMode(self):
        stack = [self.root]
        count = {}

        while stack:
            cur_node = stack.pop()
            count[cur_node.data] = 1 + count.get(cur_node.data, 0)
            print(count)
            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)
        max_val = []
        for key in count.keys():
            if count[key] == 2:
                max_val.append(key)
        return max_val
    
    
    def minDiffInBST(self) -> int:
        stack = [self.root]
        total_diff = 1_000_000
        queue = deque()
        queue += [self.root]
        
        while queue:
            node = queue.popleft()
            while stack:
                cur_node = stack.pop()
                if cur_node.left:
                    if (node.data - cur_node.left.data) < total_diff:
                        total_diff = abs(node.data - cur_node.left.data)
                    stack.append(cur_node.left)
                if cur_node.right:
                    if abs(cur_node.right.data - node.data) < total_diff:
                        total_diff = abs(cur_node.right.data - node.data)
                    stack.append(cur_node.right)
            stack = [self.root]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return total_diff
    
    
    

if __name__ == "__main__":
    tree = BinarySearchTree()
    # tree.append(4)
    # tree.append(2)
    # tree.append(7)
    # tree.append(1)
    # tree.append(3)
    # tree.append(6)
    # tree.append(9)
    # tree.append(27)
    # tree.append(34)
    # tree.append(58)
    # tree.append(50)
    # tree.append(44)
    # tree.append(52)
    tree.append(3)
    tree.append(9)
    tree.append(20)
    tree.append(15)
    tree.append(7)
    # tree.append(2)
    # tree.invertTree()
    # print(tree.pre_order())
    # print(tree.findMode())
    # print(tree.minDiffInBST())
    # print(tree.findTarget(4))
    # print(tree.max())
    # tree.delete(90)
    # print(tree.min())
    # print(tree.search(20))
    # print(tree.left(45))
    # print(tree.right(97))
    # print(tree.left_sum())
    # print(tree.min_diff())
    print(tree.pre_order())
    # print(tree.iin_order())
