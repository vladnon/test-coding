from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
        
    def append(self, data):
        cur_node = self.root
        new_node = Node(data)
        
        if not self.root:
            self.root = new_node
            return
        
        while cur_node:
            if not cur_node.left:
                cur_node.left = new_node
                return
            elif not cur_node.right:
                cur_node.right = new_node
                return
            else:
                cur_node = cur_node.left
                
                
    def print(self):
        queue = deque()
        queue.append(self.root)
        result = []
        
        while queue:
            cur_node = queue.popleft()
            result.append(cur_node.data)
            if cur_node.left:
                queue.append(cur_node.left)
            if  cur_node.right:
                queue.append(cur_node.right)
        return result
    
    def average_of_every_level(self):
        queue = []                  
        queue.append(self.root)
        level = []
        result = []
        
        while queue:
            size = len(queue)
            
            while size > 0:
                cur_node = queue.pop()
                level.append(cur_node.data)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
                size -= 1
            result.append(sum(level) / len(level))
            level = []
        return result
    
    
    def max_level_sum_binary_tree(self):
        queue = deque()
        queue += [self.root]
        level = []
        count_level = 0
        max_sum = 0
        result = 0

        while queue:
            size = len(queue)

            while size > 0:
                cur = queue.popleft()
                level.append(cur.data)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
            count_level += 1
            if sum(level) > max_sum:
                max_sum = sum(level)
                result = count_level
            level = []
        return result
    
    
    def max_level_sum_binary_tree(self):
        queue = deque()
        queue += [self.root]
        levels = {}
        level = []
        count_level = 0

        while queue:
            size = len(queue)

            while size > 0:
                cur = queue.popleft()
                level.append(cur.data)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
            levels[sum(level)] = count_level
            count_level += 1
            level = []
        return levels[max(levels.keys())]
    
    def kth_smallest_node(self, k):
        queue = deque()
        queue += [self.root]
        count = 0
        # cur = root

        while queue or count < k:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            count += 1
        return cur.data
    def return_levels(self):
        queue = deque([self.root])
        level = []
        result = []

        while queue:
            size = len(queue)

            while size > 0:
                cur = queue.popleft()
                level.append(cur.data)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                size -= 1
            result.extend([level])
            level = []
        return result
    
    def is_uni_valued(self):
        queue = deque()
        val = self.root.data

        while queue:
            cur = queue.popleft()
            if val != cur.data:
                return False
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
                
        return True
    def min_depth(self):
        queue = deque([self.root])
        count = 1

        if not self.root:
            return 0

        while queue:
            cur = queue.popleft()
            if not cur.left and not cur.right:
                return count
            if cur.right:
                queue.append(cur.right)
            if cur.left:
                queue.append(cur.left)
            count += 1
            
    
    def is_cousins(self, x, y):
        queue = deque([self.root])
        parents = {}
        levels = {}
        count = 0
        
        while queue:
            size = len(queue)
            while size > 0:
                cur = queue.popleft()
                levels[cur.data] = count
                if cur.left:
                    queue.append(cur.left)
                    parents[cur.left.data] = cur.data
                if cur.right:
                    queue.append(cur.right)
                    parents[cur.right.data] = cur.data
                size -= 1
            count += 1
        if parents[x] != parents[y] and levels[x] == levels[y]:
            return True
        return False
    
    
    def second_min_val(self) -> int:
        queue = deque([self.root])
        result = set()

        while queue:
            cur = queue.popleft()
            result.add(cur.data)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        result.remove(3)
        if result == set():
            return -1
        return min(result)
    
if __name__ == "__main__":
    tree = BinaryTree()
    tree.append(3)
    tree.append(9)
    tree.append(20)
    tree.append(15)
    tree.append(7)
    tree.append(21)
    print(tree.print())
    print(tree.average_of_every_level())
    print(tree.max_level_sum_binary_tree())
    print(tree.kth_smallest_node(1))
    print(tree.return_levels())
    print(tree.is_uni_valued())
    print(tree.min_depth())
    # print(tree.is_cousins(15, 21))
    print(tree.second_min_val())
    
nums = set()
min(nums)