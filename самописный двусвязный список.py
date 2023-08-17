# пока я лох, сделал не правильно относительно сложности алгоритмов
class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
        self.prev = None
        
class DbLinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            cur_node = self.head
            new_node = Node(data)
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None
            
            
    def extend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
    def print(self):
        cur_node = self.head
        output = ''
        while cur_node:
            print(cur_node.data, end = ', ')
            cur_node = cur_node.next
        print()
        
        
        
    def remove_first(self):
        cur_node = self.head
        self.head = cur_node.next
        cur_node.prev = self.head
        
    def remove_last(self):
        cur_node = self.head
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        cur_node.next = None
        
    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.next is not None:
            if count == index:
                self.remove_first()
                return
            
            elif count + 1 == index:
                the_node_to_remove = cur_node.next
                the_node_after_removed = the_node_to_remove.next
                cur_node.next = the_node_after_removed
                the_node_after_removed.prev = cur_node
                return
            
            count += 1
            cur_node = cur_node.next    
        raise IndexError("Вы вышли за поля списка")
    
    
    def insert(self, data, index):
        cur_node = self.head
        new_node = Node(data)
        count = 0
        while cur_node.next is not None:
            if count == index:
                self.extend(data)
                return
            
            elif count + 1 == index:
                the_node_after_new = cur_node.next
                cur_node.next = new_node
                the_node_after_new.prev = new_node
                new_node.next = the_node_after_new
                new_node.prev =  cur_node
                return
            
            count += 1
            cur_node = cur_node.next    
        raise IndexError("Вы вышли за поля списка")
    
    def len(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            cur_node = cur_node.next
            count += 1
        print(count)
        
    def value(self, index):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if count == index:
                print(cur_node.data)
                return
            count += 1
            cur_node = cur_node.next
        raise IndexError("Вы вышли за поля списка")
    
if __name__ == "__main__":
    nums = DbLinkedList()
    
    nums.append(5)
    nums.append(35)
    nums.append(98)
    nums.append(456)
    nums.append(34)
    
    nums.extend(1)
    
    nums.remove(1)
    
    nums.insert(21, 1)
    
    nums.remove_first()
    
    nums.remove_last()
    
    nums.print()
    
    nums.len()
    
    nums.value(3)