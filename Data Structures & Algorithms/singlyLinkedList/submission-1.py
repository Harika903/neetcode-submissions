class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        c = self.head.next
        i = 0
        while c:
            if i == index:
                return c.val
            i += 1
            c = c.next
        return -1 

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next: 
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        c = self.head
        while i < index and c:
            i += 1
            c = c.next
    
        if c and c.next:
            if c.next == self.tail:
                self.tail = c
            c.next = c.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        c = self.head.next
        result = []
        while c:
            result.append(c.val)
            c = c.next
        return result