    
from collections import deque, Counter

def pohuy(nums:list[int]) -> list[int]:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for key in count.keys():
        if count[key] > 1:
            return key
    
def djakstra(graph: dict[dict], start: int, target: int) -> list[int]:
    costs = {node: float("inf") for node in graph}
    costs[start] = 0
    
    parents = {node: -1 for node in graph}
    queue = deque([(0, start)])
    
    while queue:
        cost, node = queue.popleft()
        
        for neightbor, neightbor_cost in graph[node].items():
            new_cost = cost + neightbor_cost
            if new_cost < costs[neightbor]:
                costs[neightbor] = new_cost
                parents[neightbor] = node
                queue.append((new_cost, neightbor))
            
    path = []
    cur_node = target
    while cur_node != -1:
        path.append(cur_node)
        cur_node = parents[cur_node]
        
    path.reverse()
    
    return path

if __name__ == "__main__":
    # print(uniqueOccurrences([1,2,2,1,1,3]))
    # name = input()
    # print(f"Hello, {name}")
    print(pohuy([1,2,3, 3]))
    # pohuy([3, 1, 3, 1, 1])
    graph = {
        1: {2: 1, 3: 3},
        2: {1: 1, 4: 4, 3: 1},
        3: {1: 1, 4: 2, 2: 1},
        4: {2: 4, 3: 2}
    }
    
    print(djakstra(graph, 1, 4))



        

        

