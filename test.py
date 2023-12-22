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
   
# if __name__ == "__main__":
    
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
    
