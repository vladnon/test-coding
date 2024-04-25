class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        
        
class BinaryHeap:
    def __init__(self, name) -> None:
        self.nodes = []
        self.name = name
        
        
    def sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.nodes[parent].key < self.nodes[idx].key:
                self.nodes[parent], self.nodes[idx] = self.nodes[idx], self.nodes[parent]
                idx = parent
            else:
                break
            
    def sift_down(self, idx):
        n = len(self.nodes)
        while idx < n:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left <= n - 1 and self.nodes[left].key > self.nodes[largest].key:
                largest = left
            if right <= n - 1 and self.nodes[right].key > self.nodes[largest].key:
                largest = right 
            if largest != idx:
                self.nodes[idx], self.nodes[largest] = self.nodes[largest], self.nodes[idx]
                idx = largest
            else:
                break
        
    def append(self, key, value):
        self.nodes.append(Node(key, value))
        idx = len(self.nodes) - 1
        self.sift_up(idx)
    
    def pop_max(self):
        result = self.nodes[0]
        
        self.nodes[0] = self.nodes.pop()
        self.sift_down(0)
        return result
    
    def found_by_idx(self, key):
        for idx in range(len(self.nodes)):
            if self.nods[idx].key == key:
                return idx  
            
    def heap_recovery(self, idx):
        if (idx - 1) // 2 >= 0 and self.nodes[(idx - 1) // 2] > self.nodes[idx].key:
            self.sift_up(idx)
        self.sift_down()
    
    def remove(self, key):
        idx = self.found_by_idx(key)
        self.nodes[idx] = self.nodes.pop()
        self.heap_recovery(idx)

    
    def retur(self):
        return f"{(self.name ,[(node.key, node.value) for node in self.nodes])}"
    
    def heapify(self, array):
        self.nodes = []
        for num in array:
            self.nodes.append(Node(num))
        
        
    
if __name__ == "__main__":
    heap = BinaryHeap('Сделать этот проект')
    heap.append(5, "написать версию для терминала")
    heap.append(3, "Написать визуал")
    heap.append(10, "соединить все части проекта")
    print(heap)