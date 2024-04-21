from binary_heap import *
from heapq import *
# Арифметические алгоритмы

# Нахождение всех делителей
# после n//d, нет смысла идти тк они будут повторятся, соотвестно сложность будет O(sqrt(n))
def dividers(n):
    result = set()
    d = 1
    while d * d <= n:
        if n % d == 0:
            result.add(d)
            result.add(n // d)
        d += 1
    return result

# Простое ли число
# ну тут тоже самое, можно просто перебором, но тогда сложность будет O(n), а можно как и с делителями

def isprime(n):
    d = 2
    while d <= (n // d) + 1:
        if n % d == 0:
            return False
        d += 1
    return True

# Решето Эратосфена
# нужен если нужно определить большое количество чисел в диапозоне
def isprime_diap(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    for index in range(2, n + 1):
        if primes[index]:
            for idx in range(index * index, n + 1, index):
                primes[idx] = False
    result = [i for i in range(n + 1) if primes[i]]
    return result


# Разложение на простые множители
def factor(n):
    result = []
    d = 2
    
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result

# Алгоритм евклида
# a // b == a = b * q + r, где q какое-то число, а q - остаток, и тогда если делить меньшее делить на остаток, 
# до того как остаток не будет равен нулю, то меньшее будет наибольшим общим делителем
def gcd(a, b):
    if max(a, b) % min(a, b) == 0:
        return min(a, b)
    return gcd(min(a, b), max(a, b) % min(a, b))

#  lcm * gcd = a * b => lcm = a * b // gcd
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Сортировки

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
    for idx in range(len(nums)):
        cur_elem = nums[idx]
        sorted_idx = idx - 1
        
        while sorted_idx >= 0 and cur_elem < nums[sorted_idx]:
            nums[sorted_idx + 1] = nums[sorted_idx]
            sorted_idx -= 1
        nums[sorted_idx + 1] = cur_elem
    return nums

# shell sort
# тоже самое, что и сортировка вставками, только есть сначала соритрует не по всему массиву, а только по интервалам
# сначала интервал равен половине длины массива, на второй итерации половине половине прошлой половине
# на последней итерации всегда будет сравниваться весь массив, то есть просто сортировка вставками 
def shell_sort(nums: list[int]) -> list[int]:
    gap = len(nums) // 2
    while gap > 0:
        for idx in range(gap, len(nums)):
            cur_value = nums[idx]
            position = idx
            
            while position >= gap and nums[position - gap] > cur_value:
                nums[position] = nums[position - gap]
                position -= gap
            nums[position] = cur_value
        gap //= 2
    return nums
                
# Сортировка бинарной кучей
# Работает просто: по массиву создает кучу, далее вытаскиваем из нее максимальное значение, на его место встает последний элемент,
# далее совершается просивание вниз, и так пока куча не будет пустой

# Из своего модуля

class Node(Node):
    def __init__(self, data) -> None:
        super().__init__(data)

class BinaryHeap(BinaryHeap):
    def __init__(self) -> None:
        super().__init__()
        self.nodes = []

    def heap_sort(self, nums):
        self.nodes = []
        for num in nums:
            self.append(num)
        idx = len(self.nodes) - 1
        result = [0] * len(self.nodes)
        while idx > 0:
            result[idx] = self.extract_max()
            idx -= 1
        result[0] = self.nodes[0].data
        return result
    
# Из встроенного модуля
def heap_sort(nums):
    heapify(nums)
    result = []
    while nums:
        result.append(heappop(nums))
    return result
        


# Сортировка слиянием
# Рекурсивно разделяет список, на меньшие списки, пока длина меньшего списка не будет равна 1
# тогда другим алгоритмом слияния двух списков в один отсортированный все эти маленькие списки объединяются в отсортированный так-же рекурсивно 

def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return merge_two_lists(merge_sort(left), merge_sort(right))


# Сортировка подсчетом
# Единственная сортировка со сложностью O(n), однако лучше на массивах, элементы которых находятся в маленьком диапозоне
# Сначала создаю новый массив с длинной max(num) - min(nums) + 1 с нулями, далее нужно пройтись по данному массиву, и записать, сколько раз 
# появляется данный элемент, и это количество в новый массив по индексу cur_num - min(nums) + 1, наконец нужно совершить проход по новому массиву,
# и добавлять элемент idx_nums + min(nums), до тех пор пока в текущей ячейке не будет 0
# в этой сортировке не используется сравнение ключей, что делает ее уникальной.
def count_sort(nums: list[int]) -> list[int]:
    max_val = max(nums)
    min_val = min(nums)
    idx = 0
    
    new = [0] * ((max_val - min_val) + 1)

    for num in nums:
        new[num - min_val] += 1
    
    
    for index in range(len(new)):
        for elem in range(new[index]):
            nums[idx] = index + min_val
            idx += 1
    return nums


# def count_sort_odd_even(nums: list[int]) -> list[int]:
#     max_val = max(nums)
#     min_val = min(nums)
#     idx = 0
    
#     odd = [0] * ((max_val - min_val) + 1)
#     even = [0] * ((max_val - min_val) + 1)

#     for num in nums:
        
#         odd[num - min_val] += 1
    
    
#     for index in range(len(odd)):
#         for elem in range(odd[index]):
#             nums[idx] = index + min_val
#             idx += 1
#     return nums

# Слияние двух списков
# Алгоритм двух указателей, двигаем указатели в двух списках сначала, если первый поинтер меньше, то добавляем элемент в массив, который потом будет 
# возвращен, и двигаем указатель право на один, и так в друг списках пока поинтеры не дайдут до конца списка

def merge_two_lists(list1: list[int], list2: list[int]) -> list[int]:
    p1 =  p2 = 0
    result = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    while p1 < len(list1):
        result.append(list1[p1])
        p1 += 1
    while p2 < len(list2):
        result.append(list2[p2])
        p2 += 1
    return result
# Поиски

# Бинарный поиск
# Берется среднее число, если оно равно числу, которое мы ищем, то алгоритм выполнился, т.к. мы нашли число, если число меньше, то мы отрезаем от массива все правые числа от этого элемента, и находим средний элемент уже нового массива, и так далее пока не найдем элемент



def binary_search(nums, target):
    
    new_nums = merge_sort(nums)
    
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

# Алгоритм большинства Боейра - Мура
# алгоритм таков: создаем переменные, счетчик количества вхождений элемента, и кандидат(текущий элемент), 
# у которого большинство вхождений, далее проходим по массиву, и если кандидат равен текущему элементу, 
# то логично count будет увеличиваться на 1, а если нет, то вычитаться 1. Если же count равен 0,
# то есть количество элемента уничтожило количество другого элента, далее будет рассматриваться второй элемент 
# как новый кандитат, и его count будет 1


def majority_elem(nums: list[int]) -> int:
    count = 0
    cand = None
    candidates = []
    
    for num in nums:
        if count == 0:
            cand = num
            count = 1
        elif num == cand:
            count += 1
        else:
            count -= 1
    
    # Проверяем, что кандидат действительно является мажоритарным элементом
    if nums.count(cand) > len(nums) // 2:
        candidates.append(cand)
    
    # Ищем другие кандидаты с таким же количеством вхождений
    for num in nums:
        if num != cand and nums.count(num) == nums.count(cand):
            candidates.append(num)
    
    return candidates


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

def find_num_between_target(nums, target):
    left, right = 0, len(nums) - 1
    while nums[left] != target:
        left += 1
    while nums[right] != target:
        right -= 1
    return nums[left + 1:right]

# Метод sliding window
# Например мне надо посчитать все суммы подмассивов с длиной 3, вместо того, чтобы просто проходиться несколько раз по массиву, я просто
# передвегать условный блок, на одно вправо и на одно влево, и тогда сложность будет o(n)
def fixed_sliding_window(arr: list[int], k: int) -> int:
    # считаю начальную сумму
    cur_subarr = sum(arr[:k])
    result = [cur_subarr]
    
    # начинаю двигать блок 
    for i in range(1, len(arr)-k+1):
        cur_subarr -= arr[i -1]
        cur_subarr += arr[i+k-1]

        # записываю результат в массив с результатами, и вывожу
        result.append(cur_subarr)
    return result

# Это было fixed_sliding_window - когда я знаю размер окна
# А dinamic sliding window, работает по другому, я сначала иду вправо до результата, а если меня не устраивает результат, то я двигаю левый указатель враво, до тех
# пор пока меня не устроит результат, а позже делаю тоже самое
# В этой задаче мне нужно найти минимальный размер подмассива, с суммой больше 7
def dinamic_sliding_window(arr: list[int], x: int) -> int:
    # отслеживаю минимальное значение
    min_length = float("inf")
    
    # текущее значение показателей
    left = 0
    right = 0
    curr_sum = 0
    
    # движение по блока, до того как критерии будут выполнены
    while right < len(arr):
        curr_sum += arr[right]
        right += 1
    
    # уже работа  с нужными значениями
        while left < right and curr_sum >= x:
            curr_sum  -= arr[left]
            left += 1
            
            min_length = min(min_length, right -left + 1)
    return min_length

def max_profit(prices: list[int], x:int) -> int:
    buy, sell = 0, 1
    result = 0
    
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[buy] - prices[sell]
            result = max(result, profit)
        else:
            buy = sell
        buy += 1
    return result
def countGoodSubstrings(s: str) -> int:
    left, right = 0, 3        
    count = 0
    while right < len(s) + 1:
        visited = {}
        for char in s[left:right]:
            visited[char] = 1 + visited.get(char, 0)
            
        if len(visited) == 3:
            count += 1

        left += 1
        right += 1
    return count

def lengthOfLongestSubstring(s: str) -> int:
        left, right = 0, 0
        res = 0

        while right < len(s) + 1:
            visited = {}
            for char in s[left:right]:
                visited[char] = 1 + visited.get(char, 0)

            if len(s[left:right]) == len(visited):
                res = max(res, right - left)
                right += 1
            else:
                left = right - 1
        return res

def longes_substring_of_0(s: str):
    left, right = 0, 0
    length = 0
    visited = {}

    while right < len(s):
        window = right - left
        char = s[right]
        
        visited[char] = visited.get(char, 0) + 1
        
        if len(visited) == 1:
            length = max(length, window)
            
        else:
            left = right - 1
            visited[s[left]] -= 1
        right += 1
    return length

def minSubArrayLen( target: int, nums: list[int]) -> int:
        left, right, length = 0, 0, float("inf")
        cur_sum = 0

        while right < len(nums):
            cur_sum += nums[right]

            while cur_sum > target and left <= right:
                length = min(length, right - left + 1)
                cur_sum -= nums[left]
                left += 1
                
            right += 1
            
        return length if length is not float("inf") else 0
    
def maximumSubarraySum(nums: list[int], k: int) -> int:
    left, right, res = 0, 0, 0
    n = len(nums)
    window = 0

    visited = {}

    while right < n:
        char = nums[right]
        visited[char] = 1 + visited.get(char, 0)
        window += char
        
        if right - left + 1 == k:
            if len(visited) == k:
                res = max(res, window)

            if visited[nums[left]] > 1:
                visited[nums[left]] -= 1

            else:
                del visited[nums[left]]

            window -= nums[left]
            left += 1
            
        right += 1
    return res


# также два поинтера можно использовать не как то, что ты двигаешь сравниваешь, а как рамки, например есть задача, even odd sort,
# где есть число четное нужно переместить в начало, а если нет в конец, тогда left и right будут выступать исключительно как рамки,
# а новый массив сделать из нулей с длиной n, и тогда можно будет спокойно пользоваться индексами left и right

def even_odd_sort(nums: list[int]) -> list[int]:
    left, right = 0, len(nums) - 1
    new = [0] * len(nums)
    for num in nums:
        if num % 2 == 0:
            new[left] = num
            left += 1
        else:
            new[right] = num
            right -= 1
    return new
            
        
# идея в том, что я добавляю правый новый элемент в словарь, если его там нет, если он там есть, то сразу удалять его
# из суммы и из словаря, если равен 0, то удалять, и если длинна этого валидного подмассива равна 3, записать его сумму как результат
    
if __name__ == "__main__":
    # print(bubble_sort([8, 5, 3, 7, 7 ,2]))
    # print(quick_sort([8, 5, 3, 7, 7 ,2]))
    # print(binary_search([90, 150 , 8, 5, 3, 7 , 2], 2))
    # print(linear_search([8, 5, 3, 7, 7 ,2], 8))
    # print(fib(3))
    # print(fact(5))
    # print(sum([2, 4, 6]))
    print(insertion_sort([8, 5, 3, 7, 7 ,2]))
    print(count_sort([8, 5, 3, 7, 7 ,2]))
    # print(merge_two_lists([2, 8, 8, 16], [3, 4, 5, 5, 10]))
    # print(merge_sort([8, 5, 3, 7, 7 ,2]))
    # print(majority_elem([1, 2]))
    # print(shell_sort([8, 5, 3, 7, 7 ,2]))
    heap = BinaryHeap()
    print(heap.heap_sort([8, 5, 3, 7, 7 ,2]))
    print(heap_sort([8, 5, 3, 7, 7 ,2]))
    print(find_num_between_target([1, 2, 3, 1234, "asdfas", 12341234, 4, 5, 2], 2))

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
    print(countGoodSubstrings("xyzzaz"))
    print(lengthOfLongestSubstring('abcabcbb'))
    print(longes_substring_of_0("0010001"))
    print(minSubArrayLen(7, [2,3,1,2,4,3]))
    print(maximumSubarraySum([1,5,4,2,9,9,9], 3))
    print(even_odd_sort([5, 4, 1, 10, 15, 7]))
    
    print(dividers(24))
    print(isprime(1))
    print(isprime_diap(10))
    print(gcd(152, 42))
    print(lcm(3, 9))
    print(factor(24))
    

        