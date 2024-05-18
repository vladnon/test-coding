from dataclasses import dataclass, field
from typing import List, Optional
import BinaryHeap
 
@dataclass
class TaskNode:
    key: int
    value: str
    sub_nodes: Optional[List[BinaryHeap.Node]] = field(default_factory = list) 
        
    def _sift_up(self, idx: int):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.sub_nodes[parent].key > self.sub_nodes[idx].key:
                self.sub_nodes[parent], self.sub_nodes[idx] = self.sub_nodes[idx], self.sub_nodes[parent]
                idx = parent
            else:
                break
            
    def _sift_down(self, idx: int):
        n = len(self.sub_nodes)
        while idx < n:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left <= n - 1 and self.sub_nodes[left].key < self.sub_nodes[largest].key:
                largest = left
            if right <= n - 1 and self.sub_nodes[right].key < self.sub_nodes[largest].key:
                largest = right 
            if largest != idx:
                self.sub_nodes[idx], self.sub_nodes[largest] = self.sub_nodes[largest], self.sub_nodes[idx]
                idx = largest
            else:
                break
        
    def add_new_task(self, key: int, value: str):
        self.sub_nodes.append(BinaryHeap.Node(key, value))
        idx = len(self.sub_nodes) - 1
        self._sift_up(idx)
    
    def pop_max(self) -> int:
        result = self.sub_nodes[0]
        
        self.sub_nodes[0] = self.sub_nodes.pop()
        self._sift_down(0)
        return result
    
    def _find_by_key(self, key: int) -> int:
        for idx in range(len(self.sub_nodes)):
            if self.sub_nodes[idx].key == key:
                return idx  
            
    def _heap_recovery(self, idx: int):
        if (idx - 1) // 2 >= 0 and self.sub_nodes[(idx - 1) // 2] < self.sub_nodes[idx].key:
            self._sift_up(idx)
        self._sift_down()
    
    def remove_task(self, key: int):
        idx = self._find_by_key(key)
        self.sub_nodes[idx] = self.sub_nodes.pop()
        self._heap_recovery(idx)

    
    def return_task(self):
        result = []
        for node in self.sub_nodes:
            if node.nodes:
                for node in node.nodes:
                    result.append(node.value)
            result.append(node.value)
        return result

    def heapify(self, array: list[int]):
        self.sub_nodes = []
        for num in array:
            self.add_new_task(Node(num))

    def _find_by_value(self, value: str) -> int:
        for node in self.sub_nodes:
            if node.value == value:
                return _find_by_key(node.key)



@dataclass
class Task:
    name: str
    nodes: Optional[List[TaskNode]] = field(default_factory = list) 
        
    def _sift_up(self, idx: int):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.nodes[parent].key > self.nodes[idx].key:
                self.nodes[parent], self.nodes[idx] = self.nodes[idx], self.nodes[parent]
                idx = parent
            else:
                break
            
    def _sift_down(self, idx: int):
        n = len(self.nodes)
        while idx < n:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left <= n - 1 and self.nodes[left].key < self.nodes[largest].key:
                largest = left
            if right <= n - 1 and self.nodes[right].key < self.nodes[largest].key:
                largest = right 
            if largest != idx:
                self.nodes[idx], self.nodes[largest] = self.nodes[largest], self.nodes[idx]
                idx = largest
            else:
                break
        
    def add_new_task(self, key: int, value: str):
        self.nodes.append(TaskNode(key, value))
        idx = len(self.nodes) - 1
        self._sift_up(idx)
    
    def pop_max(self) -> int:
        result = self.nodes[0]
        
        self.nodes[0] = self.nodes.pop()
        self._sift_down(0)
        return result
    
    def _find_by_key(self, key: int) -> int:
        for idx in range(len(self.nodes)):
            if self.nodes[idx].key == key:
                return idx  
            
    def _heap_recovery(self, idx: int):
        if (idx - 1) // 2 >= 0 and self.nodes[(idx - 1) // 2] < self.nodes[idx].key:
            self._sift_up(idx)
        self._sift_down()
    
    def remove_task(self, key: int):
        idx = self._find_by_key(key)
        self.nodes[idx] = self.nodes.pop()
        self._heap_recovery(idx)

    
    def return_task(self) -> List[TaskNode]:
        result = []
        for node in self.nodes:
            result.append(node.value)
            if node.sub_nodes:
                for node in node.sub_nodes:
                    result.append(node.value)
        return result

    def heapify(self, array: list[int]):
        self.nodes = []
        for num in array:
            self.add_new_task(TaskNode(num))

    def _find_by_value(self, value: str) -> int:
        for node in self.nodes:
            if node.value == value:
                return self._find_by_key(node.key)


# делает на там просеивание вниз, если пишу TaskNode._sift_up(idx) - пишет типо не хватает аргумента, тоесть туда self не передается
    def add_subtask(self, value: int, sub_key: int, sub_value):        
        idx = self._find_by_value(value)
        self.nodes[idx].sub_nodes.append(TaskNode(sub_key, sub_value))
        # TaskNode._sift_up(idx)


if __name__ == "__main__":
    heap = Task('Сделать этот проект')
    heap.add_new_task(1, "написать версию для терминала")
    heap.add_new_task(2, "Написать визуал")
    heap.add_subtask("Написать визуал", 4, "Определиться с цветами") 
    heap.add_subtask("Написать визуал", 1, "Сделать примерный макет") 
    heap.add_new_task(3, "соединить все части проекта")
    print(heap.return_task())
