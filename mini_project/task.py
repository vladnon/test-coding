from dataclasses import dataclass, field
from typing import List, Optional
from BinaryHeap import Binary_heap, Node


 
@dataclass
class TaskNode(Binary_heap, Node):
    sub_nodes: List[Node] = field(default_factory = list) 

    def add_new_subtask(self, idx: int,  sub_key: int, sub_value: str):
        self.sub_nodes.append(Node(sub_key, sub_value))
        self._sift_up(len(self.sub_nodes) - 1)

@dataclass
class Task(Binary_heap):
    task_nodes: List[TaskNode] = field(default_factory = list) 

    def __post_init__(self):
        self.task_nodes = self.nodes 

    def add_new_task(self, key: int, value: str):
        new_task = TaskNode(key, value)
        self.task_nodes.append(new_task)
        idx = len(self.nodes) - 1
        self._sift_up(idx)
    
    def add_subtask_in_heap(self, value: int, sub_key: int, sub_value: str):        
        idx = self._find_by_value(value)
        self.nodes[idx].add_new_subtask(idx, sub_key, sub_value)

    def return_task(self) -> List[Node]:
       result = []
       for node in self.task_nodes:
            result.append(node.value)
            print(node.sub_nodes)
            if len(node.sub_nodes) > 0:
                for node in node.sub_nodes:
                    result.append(node.value)
       return result



if __name__ == "__main__":
    heap = Task()
    heap.add_new_task(1, "написать версию для терминала")
    heap.add_new_task(2, "Написать визуал")
    heap.add_subtask_in_heap("Написать визуал", 4, "Определиться с цветами") 
    heap.add_subtask_in_heap("Написать визуал", 1, "Сделать примерный макет") 
    heap.add_new_task(3, "соединить все части проекта")
    print(heap.return_task())
