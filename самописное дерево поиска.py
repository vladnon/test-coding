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
                    return cur_node.data
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

    def delete(self, data: int):
        cur_node = self.root
        if not self.root:
            return 
        while cur_node:
            if cur_node.left:
                if cur_node.left.data == data:
                    if cur_node.left.right:
                        cur_node.left = cur_node.left.right
                        return 
                    
                    else:
                        cur_node.left = None
                        return 
                    
            if cur_node.right:     
                if cur_node.right.data == data:
                    if cur_node.right.left:
                        cur_node.right = cur_node.right.left
                        return 
                    else:
                        cur_node.right = None
                        return 
                    
            if data < cur_node.left.data:
                cur_node = cur_node.left

            else:
                cur_node = cur_node.right
        return 
    
    # этот метод не правильный, нужно завтра доделать
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
    
    # я хочу написать метод print, чтобы вывести все узлы в отсортированном ввиде(в таком, котором они находятся в дереве)
    # но для этого мне нужно узнать как написать полный перебор дерева, а потом перевернуть путь, как в алгоритмы дейкстры
    
if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.append(90)
    tree.append(50)
    tree.append(45)
    tree.append(20)
    tree.append(76)
    tree.append(91)
    tree.append(120)
    tree.append(250)
    print(tree.max())
    tree.delete(50)
    print(tree.min())
    # print(tree.search(20))
    print(tree.left(90))
    print(tree.right(90))
    
    
