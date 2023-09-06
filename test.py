from collections import deque

def algorithm(graph, start, end):
    costs = {node: float("inf") for node in graph}
    costs[start] = 0    

    parents = {node : -1 for node in graph}
    queue = deque([(0, start)])
    while queue:
        cost, node = queue.popleft()

        for neighbor, weight in graph[node].items():
            new_cost = weight + cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
                queue.append((new_cost, neighbor))

    cur_node = end
    path = []
    while cur_node != -1:
        path.append(cur_node)
        cur_node = parents[cur_node]
        
    path.reverse()

    return path

def find_after_sorting(nums: list[int], target: int) -> list[int]:
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    result = []

    while left <= right:
        mid = (left + right) // 2
        guess = nums[mid]
        if guess > target:
            right = mid - 1
        elif guess < target:
            left = mid + 1
        else:
            idx = 0
            for num in nums:
                if num == target:
                    result.append(idx)
                idx += 1
            return result
    return result

# def binary_search(nums, target):
    
#     new_nums = merge_sort(nums)
    
#     if len(nums) <= 1:
#         return nums
    
#     left = 0
#     right = len(nums) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         guess = new_nums[mid]
        
#         if guess == target:
#             return f"Вы нашли число {target}, под индексом {nums.index(target)}"
        
#         if guess > target:
#             right = mid - 1
            
#         else:
#             left = mid + 1
            
#     return f"Вы не нашли число"


if __name__ == "__main__":
    

    graph = {
        1 : {2 : 5, 3 : 1},
        2 : {4 : 2, 3 : 3}, 
        3 : {2 : 3, 4 : 6},
        4 : {2: 2, 3: 6}
    }

    # print(algorithm(graph, 1, 4))
    print(find_after_sorting([1, 2, 3, 4, 2], 2))
    


        

        

