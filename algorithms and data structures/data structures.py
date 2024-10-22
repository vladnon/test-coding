# Linked_list(Связный список)
# В отличие от массива, в элементах связного списках храниться не только информация(состояние, дата), а еще и ссылка на следующий элемент, это позволяет следующему обьекту массива быть в другом месте в памяти
# тебе надо еще посмотреть уроков, т.к. в этом уроке все методы твоего листа линейные( O(n) ), то есть зависят от количества элементов в листе, а по сути какие-то должны быть константные( O(1) )
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self) -> None:
        self.head = None

    # тоесть мы добавляем новый элемент в конец, мы провяет при помощи цикла while, с head до конца списка, где атрибут data будет равен none(то есть будет пустая ячейка в памяти), а если в списке ничего нет, то head списка становится новым элементом
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node
            return
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    # проходит по списку, и добавляет каждый элемен в строку, а потом просто выводит стркоу
    def print(self):
        cur_node = self.head
        output = ""
        while not cur_node:
            output += str(cur_node.data) + " -> "
            cur_node = cur_node.next
        print(output)

    # проходит по списку, через каждый элемент прибавляет переменной  count один и в конце выводит, все просто
    def len(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count

    # перезаписывает первое значение
    def extend(self, data):
        cur_node = self.head
        new_node = Node(data)
        new_node.next = cur_node
        self.head = new_node

    # проходит по списку, и оставляет в ссылку предпоследнего элемента на последний ничего не оставляет, и последний элеменет просто удаляется
    def remove_back(self):
        cur_node = self.head
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        cur_node.next = None

    # в head просто оставляет ссылку на второй элемент, и первый просто удаляется из памяти
    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.next

    def value(self, index):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if count == index:
                return cur_node.data
            count += 1
            cur_node = cur_node.next
        raise IndexError(f"Число под индексом {index} - не найдено")

    def insert(self, index, data):
        cur_node = self.head
        new_node = Node(data)
        count = 0
        while cur_node.next is not None:
            if count == index:
                self.extend(data)
                return
            elif count + 1 == index:
                node_after_cur = cur_node.next
                cur_node.next = new_node
                new_node.next = node_after_cur
                return
            count += 1
            cur_node = cur_node.next
        raise IndexError("Индекс вышел за поля списка")

    def remove(self, index):
        cur_node = self.head
        count = 0
        if count == index:
            self.remove_front()
            return
        while cur_node.next is not None:
            if count == index:
                self.remove_front()
                return
            elif count + 1 == index:
                node_to_remove = cur_node.next
                node_after_removed = node_to_remove.next
                cur_node.next = node_after_removed
                return
            count += 1
            cur_node = cur_node.next
        raise IndexError("Индекс вышел за поля списка")

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            cur_node = cur_node.next


# # Двусвязный список
# #  по сути тоже самое, только у каждого обьекта есть не только ссылка на следующий элемент, но и на предыдущий
class Node:  # noqa: F811
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class dbLinkedList:
    def __init__(self) -> None:
        self.head = None

    # если список пустой(то есть основание списка, ничему не равно или же равно None), то мы говорим что основание будет новым элементом, а предыдущего элемента нет
    #  если же список не пустой, то мы проходим по списку до последнего элемента, и говорим что следующий элемент от настоящего - новый элемент, а предыдущий от нового - настоящий, а также следующего элемента от нового - нет
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node
            new_node.next = None

    # если список пустой, то следующий элемент от нового будет основание списка , а оно в тоже время будет новым элементом
    # если список не пус той, то предыдущий элемент от основание списка будет новый элемент, а следующим от нового - основание, а также основание будет нашим новым элементом
    def extend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    # тут также все просто: проходим по списку до последнего элемента и каждый добавляет к строке, а потом ее выводим(либо просто выводим элементы типа int), в общем все также как и в односвязном списке
    def print(self):
        # cur_node = self.head
        # output = ''
        # while cur_node:
        #     output += str(cur_node.data) + ' -> '
        #     cur_node = cur_node.next
        # print(output)
        cur_node = self.head
        while cur_node is not None:
            print(cur_node.data, end=", ")
            cur_node = cur_node.next
        print()

    def len(self):
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.next
        print(count)


# Hashmap
# это структура даннх которое стоится по типу key:value, значение может быть во избежания колозий(когда ключ один и тотже ) связным списком, а ключи просто массив, они сначала хашируются под 32 бита, и получается что они нумеруются по порядку, как индексы в массиве
# хэширование - перевод из даннах из неограниченного кол-во памяти в определенный(ну в случае хэш таблицы 32 бита, а так их может быть намного больше)
# решение задачи majnority element(элемент у которого максимальное колво вхождений)
def majority_element(nums: list[int]) -> int:
    count = {}
    res, maxcount = 0, 0
    for num in nums:
        count[num] = 1 + count.get(num, 0)
        if count[num] > maxcount:
            res = num
            maxcount = count[num]
    return res


# так создается хэш-таблица
d = {}
# или
d = dict()
# чтобы добавить туда состояние, нужно сделать такую запись
d["smth"] = 0
# print(d)
d["zero"] = 1
# чтобы вывести по ключу, нужно просто сделать срез
# print(d["zero"])
# функция, чтобы проверить голосовал ли какой-то человек когда то или это первый раз
voted = {}
voted["vlad"] = True
voted["gleb"] = True
voted["peter"] = True
voted["elena"] = True
voted["anton"] = True


def check(name):
    if voted.get(name):
        return f"{name} cant vote"
    else:
        voted[name] = True
        return f"{name} cant vote"


# print(check("ok"))
# print(voted["ok"])


def get_data_from_server():
    return "getting data from server...... /n finished"


cache = {}


def hash_check(cache, url):
    if hash.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


def two_sum(nums: list[int], target: int) -> list[int]:
    count = {}
    for indx, num in enumerate(nums):
        count[num] = indx
        difference = target - num
        if difference in count:
            return [count[difference], count[num]]
    return []


# коллизия - это когда в одну ячейку массива, где хранятся ключи, вводится два элемента. Простейшим решением является создать там связнный список из двух этих элементов
# чтобы вычеслить кооф наполнения надо поделить количество элементов в хэш таблице на общее количество элементов
# нужно чтобы он был > 1, т.к. число коллизий увеличивается и быстродействинность тоже ухудшается, если например кооф наполнениея равен 3/4 то нужно увеличить количество элементов в хэш таблице


# графы - просто набор взаимосвязий с элементами, которые называются узлами, а ссылка называется ребром
# есть несколько типов графов, например ориентировынныйй граф и нет. Ориентированный граф - граф в которой ребра имеют направление(тоесть от какого узла по какой)  от A до B, а не ориентированный граф может идти в обе стороны, то есть от A до B и обратно
# и еще есть взешенный граф - у каждого его ребра есть вес(и невзвешенный соответсвенно), и цикличный и ацикличный соответственно
# вообще графы интересная тема, и я бы мог начать писать самописный граф, но так как я знаю что такое хэш-таблица и по сути графы - это абстрактная стуктура дынных , я могу сделать это проще
# невзевешеннный ацикличный ориентированный граф
graph1 = {1: [2], 2: [3], 3: []}
# взевешеннный цикличный неориентированный граф
graph2 = {
    1: {2: 3, 3: 1},
    2: {1: 3, 4: 2, 3: 1},
    3: {1: 1, 4: 5, 2: 1},
    4: {2: 2, 3: 5},
}


# Я тебя поздравляю, ты подошел к деревьям
# кстати ты не писал ни стэк, ни очередь, ни хэш таблицу,ни хэш сет, хотя понимашь как работают эти структуры данных
# их кстати много бывает, а так как ты очень давно не писал код, ты вероятно напишешь их всех
# по сути дерево почти лучшая структура данных, тк у него все действия O(log n)
# дерево всегда отсортировано, это работает по принципу, того что у узла есть только два ребенка и левый всегда меньше чем родитель, а
# а правый всегда больше, то есть поиск в нем будет как в бинарном поиске(отметает те которые больше(меньше) чем искомое)


# у узла в дереве есть информация(data), и два ребенка слева(left) и справа(right), собственно изначально они ничего не равны, тк их нет
class Node:  # noqa: F811
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


# первый элемент, и самый верхний, называется корнем, а если у узла нет детей или один ребенок, то он называется листом
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    # работает так: создает узел, и тут две ситуации: если дерево путое, то создает ему корень из этой ноды, и если нет, тут еще два случая:
    # если новый узел, если меньше чем его родитель, то тут еще две ситуции, если все слоты для детей узла заняты, то идет вглубь дерева по
    # по меньшем детям, а если нет, то создает левого ребенка узла, и если больше, ну тоже самое только наобор
    def add(self, data: int) -> None:
        # создает новый узел
        node = Node(data)
        # если нет корня, то есть дерево пустое, то новый узел будет корнем
        if not self.root:
            self.root = node
        # если нет, то создает нынешний узел(изначально равен корню), и запускает бесконечный цикл
        else:
            cur_node = self.root
            while True:
                # если значение узла, меньше его родителя, и слоты на детей узла не забиты, к родителю добавляется левая нода
                if data < cur_node.data:
                    if not cur_node.left:
                        cur_node.left = node
                        break
                    # если же заняты, то идем вглудь дерева, по левым нодам, до того пока слоты не будут открыты
                    else:
                        cur_node = cur_node.left
                # если значение узла, больше его родителя, и слоты на детей узла не забиты, к родителю добавляется правая нода
                else:
                    if not cur_node.right:
                        cur_node.right = node
                        break
                    # если же заняты, то идем вглудь дерева, по правым нодам, до того пока слоты не будут открыты
                    else:
                        cur_node = cur_node.right

    # при помощи первого метода, все остальные методы будут легкими, работает как в бинарном поиске
    def search(self, target: int) -> bool:
        # создает нынешнюю ноду
        cur_node = self.root
        # цикл до конца дерева
        while cur_node:
            # если значение ноды равно цели, то выход из метода
            if target == cur_node.data:
                return True
            # если же цель меньше нынешней ноды, мы идем к левому(меньшему) ребенку
            elif cur_node.data > target:
                cur_node = cur_node.left
            # и наоборот
            else:
                cur_node = cur_node.right
        return False

    # все методы здесь работают по принципу бинарного поиска, из-за отсортированности
    def max(self) -> int:
        # создает нынешнюю ноду
        cur_node = self.root
        # если дерево не пустое, то мы запустикаем цикл до конца дерева
        if self.root:
            while cur_node:
                # самые большие значения будут только справа, так что туда он и идет
                if cur_node.right:
                    cur_node = cur_node.right
                # если же это лист, то возвращет его значение
                else:
                    return cur_node.data
        return None

    def min(self) -> int:
        # создает нынешнюю ноду
        cur_node = self.root
        # если дерево не пустое, то мы запустикаем цикл до конца дерева
        if self.root:
            while cur_node:
                # самые меньшие значения будут только слева, так что туда он и идет
                if cur_node.left:
                    cur_node = cur_node.left
                # если же это лист, то возвращет его значение
                else:
                    return cur_node.data
        return None

    def hasnext(self, data: int) -> bool:
        # создает нынешнюю ноду
        cur_node = self.root
        # цикл до конца дерева
        while cur_node:
            # после нахожления нужной ноды, проверяем есть ли у нее дети, если есть, то выход из метода(True)
            if data == cur_node.data:
                if cur_node.left or cur_node.right:
                    return True
                # тоже выход из метода(False)
                else:
                    return False
            # алгоритм поиска
            elif data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    def hasright(self, data: int) -> bool:
        cur_node = self.root
        while cur_node:
            if data == cur_node.data:
                if cur_node.right:
                    return True, cur_node.right.data
                else:
                    return False
            elif data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    def hasleft(self, data: int) -> bool:
        cur_node = self.root
        while cur_node:
            if data == cur_node.data:
                if cur_node.left:
                    return True, cur_node.left.data
                else:
                    return False
            elif data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    def ok(self, target):
        cur_node = self.root
        parents = {}
        while cur_node:
            if cur_node.data == target:
                return True
            elif cur_node.data < target:
                cur_node = cur_node.left
                if self.hasleft(cur_node.data):
                    parents[cur_node] = cur_node.left

            else:
                cur_node = cur_node.right
                if self.hasright(cur_node.data):
                    parents[cur_node] = cur_node.right

        return parents[cur_node]

    def len(self):
        count = 0
        stack = [self.root]

        if not self.root:
            return count

        while stack:
            node = stack.pop()
            count += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return count

    # неправильно
    def delete(self, data):
        cur_node = self.root
        if not self.root:
            return False

        while cur_node:
            if cur_node.left:
                if data == cur_node.left.data:
                    if cur_node.left.right:
                        cur_node.left = cur_node.left.right
                        return True

                    else:
                        cur_node.left = None
                        return True

            if cur_node.right:
                if data == cur_node.right.data:
                    if cur_node.right.left:
                        cur_node.right = cur_node.right.left
                        return True

                    else:
                        cur_node.right = None

            if data < cur_node.left:
                cur_node = cur_node.left

            else:
                cur_node = cur_node.right
        return False

    # способы обхода бинарного дерева

    # pre-order(прямой), корень, левое поддерево и наконец правое поддерево
    # стоит напомнить как работает стэк: он работает в обратном порядке от очереди, самое левое значение выйдет последним
    def pre_order(self):
        # создает стэк с корнем, откуда и будет начинаться обход
        stack = [self.root]
        # и массив с результатом
        result = []

        if not self.root:
            return []

        # пока стэк не будет пуст, будет достовать из конца стэка одно значение, которое будет нынешним, и добаляет значение в массив
        while stack:
            cur_node = stack.pop()
            result.append(cur_node.data)
            # здесь стоит вспомить правило стэка, добавив первым правое значение, оно будет рассмотрено последним, что и надо
            # то есть правое поддерево будет в любом случае рассмотрено вторым
            if cur_node.right:
                stack.append(cur_node.right)
            # а левое первым
            if cur_node.left:
                stack.append(cur_node.left)
        return result

    # in-order(симметричный), левое поддерво корень и правое подддерво, из-за это выводит значения в отсортированном в виде
    def in_order(self):
        # стэк
        stack = []
        # массив всех значений дерева
        result = []
        # в этой реализации результат будет отсортирован, так что корень надо отложить на потом, после левого поддерева
        cur_node = self.root
        if not self.root:
            raise []

        #  пока стэк и узлы не закончяться
        while cur_node or stack:
            # до конца левого поддерева узлы будут добаляться в стэк
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            # вынимает один узел из стэка, добавляем его в результат, и идем исследовать правое поддерево
            cur_node = stack.pop()
            result.append(cur_node.data)
            cur_node = cur_node.right
        return result

    # post-order(обратный), левое поддерево, правое поддерево и корень
    def post_order(self):
        stack = []
        result = []
        node = self.root

        while node or stack:
            if node:
                stack.append(node)
                result.insert(0, node.data)
                node = node.right
            else:
                cur_node = stack.pop()
                node = cur_node.left
        return result


# AVl - дерево, разновидность дерева поиска, которая имеет одно приемущество - оно самобалансируеться, то есть к обычному дереву поиска добавить
# числа от 1 до 10, то все они уйдут вглубь правого поддерева, и это дерево просто напросто превратиться в связный список, в котором все дейтсвия
# будут со сложностью O(n), а не O(log n)
# в этом дерева есть понятие высота узла, типо у самого нижнего листа будет высота 0, и тд по дереву вверх, а у отсутствовавшего узла -1
# ну то есть высота - это путь от узла до его последнего ребенка
# смысл, чтобы разница между высотами для каждого дочернего узла было меньше улюили равна 1 по мод
class Node:  # noqa: F811
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


class AVLBinaryTree:
    def __init__(self) -> None:
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))

    def balance_check(self, node):
        if not node:
            return None
        return self._height(node.left) - self._height(node.right)

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def balance(self, node):
        balance = self.balance_check(node)

        if balance > 1:
            if self.balance_check(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.balance_check(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def append(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return

        cur_node = self.root
        parent = None

        while cur_node:
            parent = cur_node

            if data < cur_node.data:
                if not cur_node.left:
                    cur_node.left = new_node
                    break
                cur_node = cur_node.left
            else:
                if not cur_node.right:
                    cur_node.right = new_node
                    break
                cur_node = cur_node.right

        self.update_height(parent)
        self.balance(parent)

    def search(self, data):
        cur_node = self.root

        while cur_node:
            if data == cur_node.data:
                return True
            if data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    def get_right(self, data):
        cur_node = self.root

        while cur_node:
            if data == cur_node.data:
                if cur_node.right:
                    return cur_node.right.data
                else:
                    return False
            if data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    def get_left(self, data):
        cur_node = self.root

        while cur_node:
            if data == cur_node.data:
                if cur_node.left:
                    return cur_node.left.data
                else:
                    return False
            if data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False


# Бинарная куча
# Дочерние элементы должны быть не больше чем родительский. Все слои заполнены узлами, кроме последнего, в нем могут быть листья.
# На последнем слою все узлы также должны быть упорядочены. Просеивание вверх - равнивается этот ключ нового узла и ключ его родителя,
# и если он больше, то меняется с ключом с родителем и тд. Просеиванием вниз -  на место ключа нового корня встает
# наибольший дочерний ключ и так пок не останется дочерних узлов.
# Используется для эффективной реализации очереди с приоритетом, а также для сортировки.

# Изменение ключа прозвольного узла, тут тоже самое или просевание вверх или вниз.

# Эту стурктуру данных можно сделать на основе массива, ну 0 элемент будет являться корнем, а дальше дочерних элемент расчитывается по формуле
# [2i + 1] для первого ну и [2i + 2] для второго дочернего элемента. Родительский узел, логично, будет вычисляться [i -1] // 2


class Nodebh:
    def __init__(self, data) -> None:
        self.data = data


class BinaryHeap:
    def __init__(self) -> None:
        # логично, изначально куча пустая
        self.nodes = []

    # идем до корня или до того как порядок в куче не будет налажен. Проверяем больше ли значение текущего элемента чем его родителя,
    # дальше меняяем если да и меняям ноду на родительскую, если нет, то и так порядок соблюден.
    def sift_up(self, idx):
        while idx > 0:
            if self.nodes[(idx - 1) // 2].data < self.nodes[idx].data:
                self.nodes[idx], self.nodes[(idx - 1) // 2] = (
                    self.nodes[(idx - 1) // 2],
                    self.nodes[idx],
                )
            else:
                break
            idx = (idx - 1) // 2

    # если левый и правый вообще существуют, то находим максимальный ключ из них(дочерних узлов), если макс элемент не остался прежним
    # то меняем текущий на макс, а потом меняем индекс текущего на макс дочерний, если нет то порядок восстановлен
    def sift_down(self, idx):
        n = len(self.nodes)
        while idx < n:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left <= n - 1 and self.nodes[left].data > self.nodes[largest].data:
                largest = left
            if right <= n - 1 and self.nodes[right].data > self.nodes[largest].data:
                largest = right
            if largest != idx:
                self.nodes[idx], self.nodes[largest] = (
                    self.nodes[largest],
                    self.nodes[idx],
                )
                idx = largest
            else:
                break

    # Вставка проиходит в последний слой, а потом идет просеивание вверх.
    def append(self, data):
        self.nodes.append(Nodebh(data))
        idx = len(self.nodes) - 1
        self.sift_up(idx)

    # Получение максимального элемента. С первым действием все просто - корень будет самым большим числом в кучи, но после он удаляется.
    # Тогда на место корня встает самый последний добавленный элемент в кучу, но опять же упорядоченность кучи будет нарушена.
    # Дальше идет происвание вниз.
    def extract_max(self):
        if len(self.nodes) == 0:
            return
        result = self.nodes[0].data
        self.nodes[0] = self.nodes.pop()
        self.sift_down(0)
        return result

    def print(self):
        result = [node.data for node in self.nodes]
        return result

    # Ну почти тоже самое, только добавляет новый элемент на первое место
    def append_and_extract_max(self, data):
        result = self.nodes[0]
        self.nodes[0] = Nodebh(data)
        self.sift_down()
        return result

    def found_by_data(self, data):
        for idx in range(len(self.nodes)):
            if self.nodes[idx].data == data:
                return idx
        return None

    # Удаление произвольного узла, на место текущего ставится последний добавленный узел, после чего выполняется или просевание вверх или вниз,
    # смотря какое свойство было нарушено.
    def remove(self, data):
        idx = self.found_by_data(data)
        if idx is None:
            return
        self.nodes[idx] = self.nodes.pop()
        self.heap_recovery(idx)

    # Смотрит есть ли родитель и его ключ меньше чем ключ текущего, нужно делать просеивание вверх, если наоборот вниз
    def heap_recovery(self, idx):
        if (idx - 1) // 2 >= 0 and self.nodes[idx].data > self.nodes[
            (idx - 1) // 2
        ].data:
            self.sift_up(idx)
            return
        self.sift_down(idx)

    # ну тут просто меняется ключ и идет восставление порядка кучи
    def change_data(self, old, new):
        idx = self.found_by_data(old)
        if idx is None:
            return
        self.nodes[idx].data = new
        self.heap_recovery(idx)


if __name__ == "__main__":
    heap = BinaryHeap()
    heap.append(10)
    heap.append(2)
    heap.append(7)
    heap.append(12)
    heap.append(5)
    print(heap.print())
    heap.extract_max()
    print(heap.print())
    heap.append(20)
    heap.append(3)
    print(heap.print())
    heap.change_data(20, 1)
    heap.remove(10)
    print(heap.print())

    # my_tree = BinarySearchTree()
    # my_tree.add(50)
    # my_tree.add(45)
    # my_tree.add(49)
    # my_tree.add(47)
    # my_tree.add(90)
    # my_tree.add(20)
    # my_tree.add(37)
    # print(my_tree.search(90))
    # print(my_tree.max())
    # print(my_tree.min())
    # print(my_tree.hasnext(90))
    # # print(my_tree.ok(1))
    # print(my_tree.hasright(45))
    # print(my_tree.len())
    # print(my_tree.delete(45))
    # print(my_tree.len())
    # print(my_tree.search(45))
    # print(my_tree.pre_order())
    # print(my_tree.in_order())
    # print(my_tree.post_order())

    # # # my_list.remove_back()

    # # my_list.remove_front()

    # # # my_list.insert(2, 17)

    # # my_list.remove(0)

    # # #  my_list.reverse()

    # # my_list.print()

    # # print(my_list.len())

    # # print(my_list.value(2))

    # # nums = dbLinkedList()

    # # nums.append(1)
    # # nums.append(45)
    # # nums.append(754)

    # # nums.extend(54)

    # # nums.len()

    # # nums.print()

    # print(majority_element([1, 2, 3, 3]))
    # print(two_sum([1, 2, 4], 6))
