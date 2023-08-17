# import string

# короче есть список и таргет, нужно вывести индексы двух чисел которые в сумме дают таргет
# def twoSum(nums: list[int], target: int) -> list[int]:
#     hashMap = {}

#     for index, num in enumerate(nums):
#         diff = target - n
#         if diff in hashMap:
#             return [hashMap[diff], i]
#         hashMap[n] = i
#     return


# nums = [2, 6, 7, 2, 1, 3]
# target = 5
# print(twoSum(nums, target))
# работает так, что бы найти подходящее число в списке, нужно из  таргета вычесть каждое число в списке, и число в списке, которое будет равно разнице

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         return head[::-1]
    
    

# if __name__ == "__main__":
#     nums = [1, 2, 3, 4]
#     nums_ = ListNode()
#     nums__ = Solution()
    
# for letter in str(string.ascii_lowercase):
#     print(str(letter))
    
    

# def lastStoneWeight(stones):
#     while len(stones) > 1:
#         y = max(stones)
#         stones.remove(y)
#         x = max(stones)
#         stones.remove(x)
#         if y > x:
#             stones.append(y - x)
#     return stones if stones else 0
            
            
    
# def sumOfMultiples(n: int):
#     nums = list(range(1, n + 1))
#     nums_new = []
#     for num in nums:
#         if num % 3 == 0  :
#             nums.remove(num)
#         elif num % 5 != 0:
#             nums.remove(num)
#         elif num % 7 != 0:
#             nums.remove(num)
#     return nums
    
        
# print(sumOfMultiples(10))


# def countOperationsToEmptyArray(nums: list[int]) -> int:
#     for num in range(len(nums) + 1):
#         for num in nums:
#             if num == min(nums):
#                 nums.remove(num)
#             elif num == min(nums):
#                 nums.remove(num)
#                 nums.insert(-1, num)
#         return num

# if __name__ == "__main__":
#     print(countOperationsToEmptyArray([3, 4, -1]))
    
# a = int(input()) 
# b = int(input()) 

# ab = list(range(b, a + 1))
# print(ab)

# l = [1, 2, 2, 3, 4, 5 ,5]

# for num in range(len(l)):
#     if l[num] == l[num + 1]:
#         l.replace(l[num], "_")
#     print(l)


# def reverseString(s:list[str]) -> None:
#     s = s[::-1]
#     return s

# print(reverseString("HEllo"))

def containsNearbyDuplicate(nums: list[int]) -> bool:
    result = False
    for num in nums:
        if nums.count(num) >= 2:
            result = True
    return result
    # return len(set(nums)) != len(nums)

print(containsNearbyDuplicate([1,2,3,1,2,3]))
