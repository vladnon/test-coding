# Сортировка пузырьком
# просто поэтапно сравнивает левый и правый элементы массив, если левый больше, то он их меняет на правый
# и так несколько итераций пока все элементы массива не встанут на свои места
def bubble_sort(nums):
    
    if len(nums) <= 1:
        return nums
    
    swapped = True
    
    while swapped:
        swapped = False
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i+ 1], nums[i]
                swapped = True
        
    return nums
         

# Сортировка Хоара(быстрая сортировка)
# Берется любой элемент(я взял средний, но в целом можно и первый), и методом сравнений получаются два подмассива(выбранный элемент никак трогается) - в одном все элементы меньше выбранного, а вдругом наоборот, и они рекурсивно сортируются этим же алгоритмом(хотя можно и другими, но это уже будут модификации, то есть можно например их отсортировать вставками), а в итоге мы получаем отсортированный массив
def quick_sort(nums):
    
    if len(nums) < 2:
        return nums
    
    pivot = nums[len(nums) // 2]
    
    left = [e for e in nums if e < pivot]
    right = [e for e in nums if e > pivot]
    
    return ( quick_sort(left) +
            [e for e in nums if e == pivot] + 
            quick_sort(right)
            
            )
    
    
# Сортировка вставками
# кароче изначально 1 элемент масива отсортирован, и сравнивается со следущем, если он больше то норм, если меньше меняется местами с 1 и
# теперь они два отсортиванных элемента, следующий сравнивается сначала с последним из отсортированным, и если тот меньше с меньшим, и тд

def insertion_sort(nums: list[int]) -> list[int]:
    # основной цикл, который проходит по массиву, и , и 
    for idx in range(len(nums)):
        #записывает настоящее число
        cur_elem = nums[idx]
        #тк каждое новое число будет неотсортировано, то отсортировано будет число на один индекс меньше нынешнего 
        sorted_idx = idx - 1

        # цикл поиска нужного места в отсортированном подмассиве, для нового вставки нового числа
        while sorted_idx >= 0 and cur_elem < nums[sorted_idx]:
            nums[sorted_idx + 1] = nums[sorted_idx]
            sorted_idx -= 1
        nums[sorted_idx + 1] = cur_elem
    return nums


# Бинарный поиск
# Берется среднее число, если оно равно числу, которое мы ищем, то алгоритм выполнился, т.к. мы нашли число, если число меньше, то мы отрезаем от массива все правые числа от этого элемента, и находим средний элемент уже нового массива, и так далее пока не найдем элемент



def binary_search(nums, target):
    
    new_nums = quick_sort(nums)
    
    if len(nums) <= 1:
        return nums
    
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        guess = new_nums[mid]
        
        if guess == target:
            return f"Вы нашли число {target}, под индексом {nums.index(target)}"
        
        if guess > target:
            right = mid - 1
            
        else:
            left = mid + 1
            
    return f"Вы не нашли число"


# Линейный поиск
# Просто сравнивается каждое число с числом, которое мы ищем
def linear_search(nums: list[int], target) -> str:
    for num in nums:
        if num == target:
            return True
    return False

    # for num in nums:
    #     if num == target:
    #         return target
    #     else:
    #         next(nums)
    # return -1

    
    
# Рекурсия 
# По сути это функция, которое в процессе выполнение выполняет себя столько раз, пока не будет собдюдено условие
# Я рассматрю на примере числа Фибоначчи
# Число Фибоначчи - последовательность, которая начинается с 0 и 1, а следующие числа являются суммой двух предыдущих
# В этом алгоритме очень сильно вписовается рекурсия, т.к. нам надо каждый раз считать

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

def fact(num):
    if num <= 1:
        return num
    else:
        return num  * fact(num - 1)
    

# алгоритмы поиска путей в графе

# Bfs - алгоритм для поиска оптимальных путей в незвешенном графе(меньше всего сегментов), 
# работает так: в очередь типа FIFO добавляется узел, и если его нет в сет уже посещенных узлов, то алгортим идет 
# к соседнему узлу, и так далее пока он не найдет нужный узел 
# Он называется поиск в ширину, потому что сначала проходит по первостепенным узлам, потом по второстепенным и тд - то есть в ширину

from collections import deque

# def bfs(start: int, target: int, graph: dict[int]) -> bool:
#     queue = deque()
#     queue += [start]
#     visited = set()

#     while queue:
#         node = queue.popleft()
#         if node not  in visited:
#             if node == target:
#                 return True
            
#             else:
#                 queue += graph[node]
#                 visited.add(node)


#     return False

# Dfs - алгоритм, который просто ищет любой путь в невзвешенном графе
# Его реализация рекурсивная, поэтому там используется стек,
#  и работает он так: основная часть - мы проверяем является ли узел искомым(True), и проверяем есть и он в массиве уже посещенных(False),
# рекурсивная часть - ищем соседа этого узла, и если в проверка возвращается True, возвращаем тоже самое, если нет, заново, 
# пока не найдем нужный узел
# Он называется поиск в глубину, потому что просто ищет соседние узлы

def dfs(start: int, target: int, graph: dict[int], visited: list[int]):
    if start == target:
        return True
    
    if start in visited:
        return False
    
    visited += [start]
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(neighbor, target, graph, visited):
                return True
    return False
    
# Алгоритм Дейкстры - алгоритм поиска оптимального пути в взвешенном графе
# работает он так: он создает несколько словарей: словарь под длину пути(вначале он будет бесконченость для всех ребер, 
# кроме первого, он будте 0), словарь родителей узлов(вначале -1 для всех узлов, потому мы их еще не исследовали),
# и очередь(работает парой - вес и узел), после он будет перезаписыпать пути до узлов, если он короче уже исседованных, 
# и заполнять словарь с родителями, а также добавлять парами пути и узлы, и так пока очередь ну будет пуста(то есть
# пока весь граф не будет исследован)
# По сути он просто идет по путям, которые короче, и если он нашел путь, который короче уже исследованного, то просто 
# перезаписывает его путь и вес


def dijkstra(graph: dict[dict], start: int, end: int) -> list[int]:
    costs = {node: float("inf") for node in graph}
    costs[start] = 0

    parents = {node: -1 for node in graph}
    queue = deque([(0, start)])

    while queue:
        cost, node = queue.popleft()

        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
                queue.append((new_cost, neighbor))

    path = []
    cur_node = end
    while cur_node != -1:
        path.append(cur_node)
        cur_node = parents[cur_node]

    path.reverse()

    return path

# Поиск k-ближайших соседей(knn)
# Его используют в первоначальном ввиде для классификации, а с модификациями уже можно сделать и регрессию(прогназирование)
# открой рисунок с названием ""
# кароче это прям алгоритм обучения модели, так что тебе еще рано, плюс я не знаю как его написать, но как он работает могу написать
# у нас есть график, в котором помечены точки которые отвечают за разные классы(если пандас будешь учить поймешь), и точка, которая обозначает
# объект, который надо классифицировать, и все просто, первые k-ближайшие точки, и определят, что это за класс, на графике оси являются 
# признаками, что говорит мне, о том что я не просто страдаю херней, изучая статиску


if __name__ == "__main__":
    # print(bubble_sort([8, 5, 3, 7, 7 ,2]))
    # print(quick_sort([8, 5, 3, 7, 7 ,2]))
    # print(binary_search([90, 150 , 8, 5, 3, 7 , 2], 2))
    print(linear_search([8, 5, 3, 7, 7 ,2], 8))
    # print(fib(3))
    # print(fact(5))
    # print(sum([2, 4, 6]))
    print(insertion_sort([5, 1, 10, 5, -2  ]))

    graph = {
        1 : [1, 3],
        2 : [1],
        3 : [1, 3, 2]
    }

    graph_for_algorithm = {
        1: {2: 3, 3: 1},
        2: {1: 3, 4: 2, 3: 1},
        3: {1: 1, 4: 5, 2: 1},
        4: {2: 2, 3: 5}
    }
    

    # print(bfs(graph, 1, 2))
    # print(dfs(1, 3, graph, visited = []))
    # print(dijkstra(graph_for_algorithm, 1, 4))
    
    
    