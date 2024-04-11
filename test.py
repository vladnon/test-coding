
def isGood( nums: list[int]) -> bool:
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

def checkIfExist( arr: list[int]) -> bool:
        for num in arr:
            if (num * 2) in arr and num is not num:
                return True
        return False
    
    
def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for idx in range(gap, len(nums  )):
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
            target = 2*num
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

def smallerNumbersThanCurrent( nums):
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
        right = sum(nums[idx + 1:])
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

1
#         return arr

def restoreString( s: str, indices: list[int]) -> str:
        new_str = ""
        
        for idx in range(len(s)):
            new_str += s[indices[idx]]
        return new_str
     
# тоже самое только с индексом, и тогда не может быть повторений в хеш мапепншпншп, бля гений реально
def maxSum( nums: list[int]) -> int:
    hashmap = {}
    sums = set()
    max_pair = -1
    for idx in range(len(nums)):
        res = list(map(int, str(nums[idx])))
        hashmap[idx] = max(res)

    for key1, value in hashmap.items():
            sums.add(value)
            for key in hashmap.keys():
                if  hashmap[key] == value and key1 != key:
                    if max_pair < nums[key1] + nums[key]:
                        max_pair = nums[key1] + nums[key]
    return max_pair

# прально, но медленно, надо реально было бинариу серчем захерачить, ну ладно
# def replaceElements(arr: list[int]) -> list[int]:
#     for idx in range(len(arr)):
#         if idx == len(arr) -1 :
#             arr[idx] = -1
#         else:
#             max_after = max(arr[idx + 1:])
#             arr[idx], max_after = max_after, arr[idx]
#     return arr

# что пока я могу сказать, right не сбрасывается после второго цикла, так что надо что-то придумать
def replaceElements(arr: list[int]) -> list[int]:
        left, right = 0, 1
        max_right_pointer = 1
        
        while left <= len(arr):
            max_right = 0
            
            if left == len(arr) -1:
                arr[left] = -1
            while right <= len(arr) -1:
                if max_right < arr[right]:
                    max_right = arr[right]
                    max_right_pointer = right
                right += 1
            arr[left], arr[max_right_pointer] = arr[max_right_pointer], arr[left]
            left += 1
            right += 1
            max_right_pointer += 1
        return arr
    
# короче завтра доделай какая-то хуета, теперь просто добавляются какие-значения хз почему
def shortestToChar( s: str, c: str) -> list[int]:
        dists = []
        for idx in range(len(s)):
            left, right = idx, idx
            min_dist = 0
            if left == 0:
                while s[right] != c or right > len(s) - 1:
                    right += 1
                dists.append(abs(idx - right))
            if right == len(s) -1 :
                while s[left] != c or left > len(s) - 1:
                    left -= 1
                dists.append(abs(idx - left))
            else:
                while s[left] != c or left > len(s) - 1:
                    left -= 1
                while s[right] != c or right > len(s) - 1:
                    right += 1
                min_dist = min(abs(idx - right), abs(idx - left))
                dists.append(min_dist)
        return dists
            
            
def smting(s):
    count = 0
    new_str = ''
    valid = ['c', 'a', 't']
    for idx in range(len(s)):
        if s[idx] in valid and count != 3:
            if s[idx] == 'c' and count == 0:
                new_str += 'C'
                count += 1
            if s[idx] == "a" and count == 1:
                new_str += 'A'
                count += 1
            if s[idx] == 't' and count == 2:
                new_str += 'T'
                count += 1
        else:
            new_str += s[idx]
    return new_str

# короче, если сумма этих двух чисел в отсортированном массиве меньше чем цель, то автоматически можно не проходить по всем остальным числам, потому и так понятно, что их сумма будет меньше =>
# можно изменить левый указаталь и исказть новую пару, 
def countPairs( nums: list[int], target: int) -> int:
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
        
def twoSum( nums: list[int], target: int) -> list[int]:
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

# норм идея, но нужно во-первых оптимизировать, во-вторых нужны поинтеры, так как .index берешь возвращает индекс ближайщего испокомого элемента, 
# ну типо не файт, что это именно тот, который тебе нужен, ну например в случае с 266 
def largestInteger( num: int) -> int:
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
                right = len(nums) -1
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
                
    new = ''
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
    new_s = [''] * len(words)
    
    for word in words:
        idx = int(word[-1]) - 1
        new_s[idx] = word[:-1]

    return ' '.join(new_s)
    
# брат, запомни ты должен на ближайщих выходных изучить heap, потому что largest integer, хоть и круто, типо сделал сам жесткий алгоритм,
# но все равно при помощи heap было бы намного быстрее по сложности

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
    print(n_in_arr_and_double([-2,0,10,-19,4,6,-8]))
    print(search_range([5,7,7,8,8,10], 8))
    print(smallerNumbersThanCurrent([8,1,2,2,3]))
    # print(areAlmostEqual("siyolsdcjthwsiplcc j buceoxm p jgrauocx", "siyolsdcjthwsiplcc p buceoxm j jgrauocx"))
    print(middle_elem([2,3,-1,8,4]))
    print(leftRightDifference([10,4,8,3]))
    # print(shortestToChar("loveleetcode", "e"))
    # print(replaceElements([17,18,5,4,6,1]))
    print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))
    print(maxSum([8,75,28,35,21,13,21]))
    # print(replaceElements([17,18,5,4,6,1]))
    # print(frequencySort("tree"))
    print(shortestToChar("aaba", "b"))
    print(smting('catcatcat'))
    # print(smting2([8, 7, 20, 5, 17, 40], 5))
    print(twoSum([3,2,4], 6))
    print(countPairs([-1,1,2,3,1], 2))
    print(largestInteger(1234))
    print(countPairs([-1, 1, 2 , 3, 1], target=2))
    print(sortcolors([2,0,2,1,1,0]))
    print(thirdMax([1,2,-2147483648]))
    print(sortSentence("z1 z2 z3"))