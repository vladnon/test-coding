# Этот список я писал сам, с малейшими подсказками
# чтобы добавить функционал, нужно просто дописать дандер методы в оба класса(по значению), чтобы сделать список итерируемым нужно создать либо отдельный класс итератор, либо дандер метод __iter__(хотя по сути перебор по списку и так можно сделать, как и почти во всех методах, при помощи while cur_node.next is None: - то есть мы проходим по каждому элементу пока не находим, такой в котором ссылка на следующий None(то есть нет обьекта)), и так далее, например чтобы сравнивать элементы и тд(а все потому что каждый элемент экземляр класса Node, а у него нет такого функционала)

class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, data):
        cur_node  = self.head
        new_node = Node(data)
        if not cur_node:
            self.head = new_node
            return
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node
        
    def print(self):
        cur_node = self.head
        output = ''
        while cur_node is not None:
            output += f"| [{cur_node.data}] |"
            cur_node = cur_node.next
        print(output)
            
            
    def extend(self, data):
        cur_node = self.head
        new_node  = Node(data)
        new_node.next = cur_node
        self.head = new_node
        
    def len(self):
        cur_node = self.head
        counter = 0
        while cur_node is not None:
            counter += 1
            cur_node = cur_node.next
        # print(f"В вашем списке {counter} элемента")
        return counter
        
    def remove_last(self):
        cur_node = self.head
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        cur_node.next = None
        
    def remove_first(self):
        cur_node = self.head
        self.head = cur_node.next
        
    def insert(self, data, index):
        cur_node = self.head
        new_node = Node(data)
        count = 0
        while cur_node.next is not None:
            if count == index:
                self.extend(data)
                return
            
            if count  + 1 == index:
                the_node_after_cur = cur_node.next
                cur_node.next = new_node
                new_node.next = the_node_after_cur
                return
            
            cur_node = cur_node.next
            count += 1
        
        raise IndexError("Вы вышли за поля списка")
    
    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.next is not None:
            if count == index:
                self.extend()
                return
            
            if count  + 1 == index:
                the_node_to_remove = cur_node.next
                the_node_after_removed = the_node_to_remove.next
                cur_node.next = the_node_after_removed
                return
            
            cur_node = cur_node.next
            count += 1
        
        raise IndexError("Вы вышли за поля списка")
    
    
    def value(self, index):
        cur_node = self.head
        count = 0
        while cur_node.next is not None:
            
            if count == index:
                return f"Под индексом {index} стоит число {cur_node.data}"
            
            cur_node = cur_node.next
            count += 1
        
        raise IndexError("Вы вышли за поля списка")
            
            
        
    def removenthfromthend(self, n ):
        cur_node = self.head
        target = self.len() - n
        count = 0
        if n == target:
            cur_node = self.head
            count = 0
            while cur_node.next is not None:
                if count == 1:
                    self.extend()
            return True
        
        while cur_node.next is not None:
            if count  + 1 == target:
                the_node_to_remove = cur_node.next
                the_node_after_removed = the_node_to_remove.next
                cur_node.next = the_node_after_removed
                return
            
            cur_node = cur_node.next
            count += 1
        
        # raise IndexError("Вы вышли за поля списка")
        
    
    # не буду писать метод reverse, т.к. не совсем понимаю алгоритм
     
if __name__ == "__main__":
    nums = LinkedList()
    
    nums.append(1)
    nums.append(243)
    nums.append(56)
    nums.append(71)
    nums.append(4)
    
    # nums.extend(20)
    
    # nums.remove_first()
    
    # nums.remove_last()
    
    nums.insert(29, 2)
    
    # nums.remove(2)
    
    # nums.removenthfromthend(1)
    
    nums.print()
    
    # nums.len()
    
    # print(nums.value(0))
    

    

    