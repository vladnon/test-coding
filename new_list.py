

class Node:
    def __init__(self, val: None) -> None:
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self, ) -> None:
        self.head = None
        
    def append(self, val: int) -> None:
        new = Node(val)
        if not self.head:
            self.head = new
            return
        
        cur = self.head
        
        while cur.next:
            cur = cur.next
        cur.next = new
        
    def extend(self, nodes: list[int]) -> None:
        idx = 0
        nodes = [Node(num) for num in nodes]
        
        if not self.head:
            self.head = nodes[idx]
            idx += 1
        cur = self.head
        
        while cur.next:
            cur = cur.next
            
        while idx < len(nodes):
            cur.next = nodes[idx]
            idx += 1
            cur = cur.next
        
        
    def print(self) -> list[int]:
        cur = self.head
        nodes = []
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        return nodes
    

def mergeTwoLists(list1, list2):
    p1, p2 = list1.head, list2.head
    result = []
    while p1 and p2 :
        if p1.val < p2.val:
            result.append(p1.val)
            p1= p1.next
        else:
            result.append(p2.val)
            p2 = p2.next
    while p1:
        result.append(p1.val)
        p1 = p1.next
    while p2:
        result.append(p2.val)
        p2 = p2.next
    idx = 0
    list1.extend([Node(num) for num in result])
    return list1



if __name__ == "__main__":
    nums1 = LinkedList()
    nums1.extend([1, 2, 4])
    nums2 = LinkedList()
    nums2.extend([1, 3, 4])
    print(mergeTwoLists(nums1, nums2))