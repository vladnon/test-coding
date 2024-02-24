def countTriples( n: int) -> int:
    left, right = 0, n - 1
    count = 0
    while left <= right:
        cur_sum_squares = (left ** 2 + right ** 2) 
        if cur_sum_squares > n * n: 
            left += 1
        elif cur_sum_squares == n * n:
            count += 1
        else:
            right += 1
    return count

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
    print(replaceElements([17,18,5,4,6,1]))

        