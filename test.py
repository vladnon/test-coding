def isGood(nums: list[int]) -> bool:
    num = max(nums)
    if nums.count(num) == 2 and num == len(nums) - 1:
        nums.remove(num)
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        print(count.values())
        if 2 not in count.values() and 3 not in count.values():
            return True
    return False


def checkIfExist(arr: list[int]) -> bool:
    for num in arr:
        if (num * 2) in arr and num is not num:
            return True
    return False


def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for idx in range(gap, len(nums)):
            elem = nums[idx]
            position = idx

            while position >= gap and nums[position - gap] > elem:
                nums[position] = nums[position - gap]
                position -= gap
            nums[position] = elem
        gap //= 2
    return nums


def n_in_arr_and_double(arr):
    arr = sorted(arr)
    left, right = 0, len(arr) - 1
    for num in arr:
        while left <= right:
            target = 2 * num
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = 0, len(arr) - 1
    return False


def search_range(nums, target):
    left, right = 0, len(nums) - 1
    count = 2
    result = []
    while left <= right:
        if count == 0:
            return result
        mid = (left + right) // 2
        if nums[mid] == target:
            result.append(mid)
            count -= 1
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1] if result == [] else sorted(result)


def smallerNumbersThanCurrent(nums):
    count = 0
    idx = 0
    result = []
    while idx < len(nums):
        cur = nums[idx]
        for num in nums:
            if cur > num:
                count += 1
        result.append(count)
        count = 0
        idx += 1
    return result


def middle_elem(nums):
    for idx in range(len(nums)):
        left = sum(nums[:idx])
        right = sum(nums[idx + 1 :])
        if left == right:
            return idx
        left, right = 0, 0
    return -1


def leftRightDifference(nums: list[int]):
    left = 0
    right = sum(nums)
    new_nums = []
    for idx in range(len(nums)):
        left += nums[idx]
        new_nums.append(abs(left - right))
        right -= nums[idx]
    return new_nums


def restoreString(s: str, indices: list[int]) -> str:
    new_str = ""

    for idx in range(len(s)):
        new_str += s[indices[idx]]


def shortestToChar(s: str, c: str) -> list[int]:
    dists = []
    for idx in range(len(s)):
        if s[idx] != c:
            left, right = idx, idx
            lflag = False
            rflag = False
            while s[right] != c and right < len(s) - 1:
                right += 1
            if s[right] == c:
                rflag = True
            while s[left] != c and left > 0:
                left -= 1
            if s[left] == c:
                lflag = True
            if not lflag:
                dists.append(abs(idx - right))
            elif not rflag:
                dists.append(abs(idx - left))
            else:
                dists.append(min(abs(idx - right), (abs(idx - left))))

        else:
            dists.append(0)
    return dists


def smting(s):
    count = 0
    new_str = ""
    valid = ["c", "a", "t"]
    for idx in range(len(s)):
        if s[idx] in valid and count != 3:
            if s[idx] == "c" and count == 0:
                new_str += "C"
                count += 1
            if s[idx] == "a" and count == 1:
                new_str += "A"
                count += 1
            if s[idx] == "t" and count == 2:
                new_str += "T"
                count += 1
        else:
            new_str += s[idx]
    return new_str


# короче, если сумма этих двух чисел в отсортированном массиве меньше чем цель, то автоматически можно не проходить по всем остальным числам, потому и так понятно, что их сумма будет меньше =>
# можно изменить левый указаталь и исказть новую пару,
def countPairs(nums: list[int], target: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0
    while left < right:
        sum_values = nums[left] + nums[right]
        if sum_values < target:
            count += right - left
            left += 1
        else:
            right -= 1
    return count


def twoSum(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    nums = sorted(nums)
    while left <= right:
        sum_values = nums[left] + nums[right]
        print(nums[right], nums[left])
        if sum_values == target:
            return [left, right]
            left += 1
        else:
            right -= 1
    return -1


def largestInteger(num: int) -> int:
    nums = list(map(str, str(num)))
    nums = [int(num) for num in nums]

    even = [num for num in nums if num % 2 == 0]
    odd = [num for num in nums if num % 2 != 0]

    left, right = 0, len(nums) - 1

    while left < len(nums) and right >= 0:
        max_even = max(even) if len(even) > 1 else 0
        max_odd = max(odd) if len(odd) > 1 else 0

        if nums[left] % 2 == 0:
            if max_even != 0:
                same = max_even
            else:
                left += 1
                continue
        else:
            if max_odd != 0:
                same = max_odd
            else:
                left += 1
                continue

        if right != 0:
            if nums[right] == same and left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right = len(nums) - 1
                if same in odd:
                    odd.remove(same)
                else:
                    even.remove(same)
            else:
                right -= 1
        else:
            left += 1
            right = len(nums) - 1
            if same in odd:
                odd.remove(same)
            else:
                even.remove(same)

    new = ""
    for num in nums:
        new += str(num)
    return int(new)


def sortcolors(nums: list[int]) -> list[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)
    idx = 0
    while count[0] > 0:
        nums[idx] = 0
        count[0] -= 1
        idx += 1
    while count[1] > 0:
        nums[idx] = 1
        count[1] -= 1
        idx += 1
    while count[2] > 0:
        nums[idx] = 2
        count[2] -= 1
        idx += 1
    return nums


def thirdMax(nums: list[int]) -> int:
    first = 0
    second = 0
    third = 0

    nums = list(set())

    for num in nums:
        if num > first:
            third, second, first = second, first, num
        else:
            if num > second:
                third, second = second, num
            else:
                third = num
    return third


def sortSentence(s: str) -> str:
    words = s.split()
    new_s = [""] * len(words)

    for word in words:
        idx = int(word[-1]) - 1
        new_s[idx] = word[:-1]

    return " ".join(new_s)


# брат, запомни ты должен на ближайщих выходных изучить heap, потому что largest integer, хоть и круто, типо сделал сам жесткий алгоритм,
# но все равно при помощи heap было бы намного быстрее по сложности
def mostWordsFound(sentences: list[str]) -> int:
    max_lenght = 0
    for sentence in sentences:
        lenght = 0
        for char in sentence:
            if char == " ":
                lenght += 1

        max_lenght = max(max_lenght, lenght + 1)
    return max_lenght


def replaceElements(arr: list[int]) -> list[int]:
    left, right = 0, len(arr) - 1
    while left <= right:
        maxi = arr.index(min(arr))
        while right != left:
            if arr[right] > arr[maxi]:
                maxi = right
            right -= 1
        arr[left], arr[maxi] = arr[maxi], arr[left]
        left += 1
        right = len(arr) - 1
    return arr


# мне кажется я уже близко, но в целом я могу быть прав
def maxSum(nums: list[int], m: int, k: int) -> int:
    left, right = 0, 0
    count = {}
    maxs = 0

    if k == 1:
        for num in nums:
            maxs = max(maxs, num)
        return maxs

    while right < len(nums):
        if nums[right] not in count:
            count[nums[right]] = 133

            if count[nums[left]] == 0:
                del count[nums[left]]

            if right - left + 1 == k:
                if len(count) >= m:
                    maxs = max(maxs, sum(nums[left:right]))
                    left += 1
                count[nums[left]] -= 1

        else:
            count[nums[right]] += 1

        right += 1

    return maxs


#
# def topKFrequent(nums: list[int], k: int) -> list[int]:
#
#         if len(nums) == 1:
#             return nums
#
#
#         heap = BinaryHeap()
#         heap.k_freq_elem(nums, k)
#
# class Node:
#     def __init__(self, data, freq) -> None:
#         self.data = data
#         self.freq = freq
#
# class BinaryHeap:
#     def __init__(self) -> None:
#         self.nodes = []
#
#     def sift_up(self, idx):
#         while idx > 0:
#             parent = (idx - 1) // 2
#             if self.nodes[idx].freq > self.nodes[parent].freq:
#                 self.nodes[idx], self.nodes[parent] = self.nodes[parent], self.nodes[idx]
#                 idx = parent
#             else:
#                 break
#
#     def sift_down(self, idx):
#         n = len(self.nodes)
#         while True:
#             left = 2 * idx + 1
#             right = 2 * idx + 2
#             largest = idx
#             if left <= n - 1 and self.nodes[left].freq > self.nodes[largest].freq:
#                 largest = left
#             if right <= n - 1 and self.nodes[right].freq > self.nodes[largest].freq:
#                 largest = right
#             if largest != idx:
#                 self.nodes[idx], self.nodes[largest] = self.nodes[largest], self.nodes[idx]
#                 idx = largest
#             else:
#                 break
#
#     def append(self, data, freq):
#         self.nodes.append(Node(data, freq))
#         idx = len(self.nodes) - 1
#         self.sift_up(idx)
#
#     def extract_max(self):
#
#         if len(self.nodes) == 0:
#             return
#
#         result = self.nodes[0].data
#         self.nodes[0] = self.nodes.pop()
#         self.sift_down(0)
#         return result
#
#
# def k_freq_elem(self, array, k):
#      count = {}
#      for num in array:
#          count[num] = 1 + count.get(num, 0)
#      self.nodes = [Node(num, freq) for num, freq in count.items()]
#      result = []
#      while k > 0:
#          res = self.extract_max()
#          result.append(res)
#          k -= 1
#      return result
#
def eazy(a: str, b: str, k) -> bool:
    count = 0
    for char in set(a):
        if char in b:
            count += a.count(char)
    if count >= k:
        return True
    return False


if __name__ == "__main__":
    # graph = {
    #     1 : {2 : 5, 3 : 1},
    #     2 : {4 : 2, 3 : 3},
    #     3 : {2 : 3, 4 : 6},
    #     4 : {2: 2, 3: 6}
    # }

    # print(algorithm(graph, 1, 4))
    # print(countTriples(5))
    # print(isGood([2,1,2,5,2,5]))
    # print(checkIfExist([-2,0,10,-19,4,6,-8]))
    # print(n_in_arr_and_double([-2,0,10,-19,4,6,-8]))
    # print(search_range([5,7,7,8,8,10], 8))
    # print(sortcolors([2,0,2,1,1,0]))
    # print(thirdMax([1,2,-2147483648]))
    # print(sortSentence("z1 z2 z3"))
    # print(mostWordsFound(["alice and bob love leetcode","i think so too","this is great thanks very much"]))
    # print(replaceElements())
    # print(maxSum([1,1,1,2], 2, 4))
    # print(topKFrequent([-1, -1], 1))
    print(eazy("aac", "abca", 3))
