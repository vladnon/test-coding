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
    left, right = 0, len(nums) - 1
    leftSum = 0
    rightSum = 0
    while left <= right:
        leftSum += nums[left]
        rightSum += nums[right]
        if leftSum == rightSum:
            return left + 1
        left += 1
        right -= 1
    return -1
# если у тебя не получается проходиться по сумме чисел, то тогда нужно попытаться рассмотреть предпологаемое среднее число,
# и сравнать сумму до него и после, если сегодня не решишь, то реши пожалуйста завтра 
    

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