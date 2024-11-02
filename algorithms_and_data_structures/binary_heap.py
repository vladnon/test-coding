class Node:
    def __init__(self, data) -> None:
        self.data = data
        
class BinaryHeap:
    def __init__(self) -> None:
        self.nodes = []

    def sift_up(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.nodes[idx].data > self.nodes[parent].data:
                self.nodes[idx], self.nodes[parent] = self.nodes[parent], self.nodes[idx]
                idx = parent
            else:
                break

    def sift_down(self, idx):
        n = len(self.nodes)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left <= n - 1 and self.nodes[left].data > self.nodes[largest].data:
                largest = left
            if right <= n - 1 and self.nodes[right].data > self.nodes[largest].data:
                largest = right
            if largest != idx:
                self.nodes[idx], self.nodes[largest] = self.nodes[largest], self.nodes[idx]
                idx = largest
            else:
                break

    def append(self, data):
        self.nodes.append(Node(data))
        idx = len(self.nodes) - 1
        self.sift_up(idx)

    def extract_max(self):
        
        if len(self.nodes) == 0:
            return
        
        result = self.nodes[0].data
        self.nodes[0] = self.nodes.pop()
        self.sift_down(0)
        return result
    
    def extract_and_append(self, data):
        result = self.nodes[0].data
        self.nodes[0] = Node(data)
        self.sift_down(0)
        return result
    
    def remove(self, data):
        idx = self.found_by_data(data)
        
        if idx is None:
            return
        self.nodes[idx] = self.nodes.pop()
        self.heap_recovery(idx)
        
    def pop(self):
        result = self.nodes.pop()
        
        if len(self.nodes) == 0:
            return
        
        n = len(self.nodes)
        self.heap_recovery(n - 1)
        return result
    
    def found_by_data(self, data):
        for idx in range(len(self.nodes)):
            if self.nodes[idx].data == data:
                return idx
        return 
    
    def heap_recovery(self, idx):
        n = len(self.nodes)
        if (idx - 1) // 2 >= 0 and self.nodes[(idx - 1) // 2].data < self.nodes[idx].data:
            self.sift_up(idx)
            return
        self.sift_down(idx)
            
    def change_data(self, old, new):
        idx = self.found_by_data(old)
        
        if idx is None:
            return
        self.nodes[idx] = Node(new)
        self.heap_recovery(idx)

    def print(self):
        result = [node.data for node in self.nodes]
        return result
    
    
    

if __name__ == "__main__":
    heap = BinaryHeap()
    heap.append(12)
    print(heap.print())
    heap.append(14)
    heap.append(2)
    heap.append(5)
    heap.append(7)
    heap.append(20)
    print(heap.print())
    print(heap.extract_max())
    print(heap.print())
    heap.change_data(12, 0)
    heap.sift_up(-1)
    print(heap.print())
    