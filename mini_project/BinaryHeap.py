from dataclasses import dataclass, field
from typing import List, Optional
import BinaryHeap
 
@dataclass
class Node:
    key: int
    value: str
        

@dataclass
class Binary_heap:
    nodes: List[Node] = field(default_factory = list) 

    def __post_init__(self):
        if not hasattr(self, 'task_nodes'):
            self.task_nodes = self.nodes 

        
    def _sift_up(self, idx: int):
        while idx > 0:
            parent = (idx - 1) // 2
            print(self.nodes[parent])
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
        self.nodes.append(Node(key, value))
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
            
    def _find_by_value(self, value: int) -> int:
        for idx in range(len(self.nodes)):
            if self.nodes[idx].value == value:
                return idx  

    def _heap_recovery(self, idx: int):
        if (idx - 1) // 2 >= 0 and self.nodes[(idx - 1) // 2] < self.nodes[idx].key:
            self._sift_up(idx)
        self._sift_down()
    
    def remove_task(self, key: int):
        idx = self._find_by_key(key)
        self.nodes[idx] = self.nodes.pop()
        self._heap_recovery(idx)

    def heapify(self, array: list[int]):
        self.nodes = []
        for num in array:
            self.add_new_task(Node(num))

