class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        cur_node = head
        index = 0
        nums = self.quick_sort(head)

        while cur_node:
            cur_node.val = nums[index]
            index += 1
            cur_node = cur_node.next
        return head

    def print(self, head):
        cur_node = head
        result = []

        while cur_node:
            result.append(cur_node.val)
            cur_node = cur_node.next
        return result

    def quick_sort(self, head):
        nums = self.print(head)

        if len(nums) < 2:
            return nums
    
        pivot = nums[len(nums) // 2]
        
        left = [e for e in nums if e < pivot]
        right = [e for e in nums if e > pivot]
        
        return ( self.quick_sort(left) +
                [e for e in nums if e == pivot] + 
                self.quick_sort(right)
                )


if __name__ == "__main__":
    sol = Solution()

nums = [1, 2, 3, 3]
count = {}
n = max(nums)
for num in nums:
    count[num] = 1 + count.get(num, 0)
print(count)
count.pop(n)
print(count)
# for num, ct in count.items():
#     if ct == 2:
#         print("found")
#         print(num)
#         if len(nums) == num + 1:
#             print(True)
# # print(False)


    



        

        

