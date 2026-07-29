from typing import Optional


# Singly Linked List
class LinkedList:
    def __init__(self, val: int = 0, next=None):
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val)

    def print_singly(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next

    def display(self, head):
        curr = head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))

    def search(self, head, val):
        curr = head
        while curr:
            if val == curr.val:
                return True
            curr = curr.next
        return False


n5 = LinkedList(5)
n4 = LinkedList(4, n5)
n3 = LinkedList(3, n4)
n2 = LinkedList(2, n3)
n1 = LinkedList(1, n2)
head = n1

# current = head
# while current:
#     print(current.val)  # 1 2 3 4 5
#     current = current.next

ll = LinkedList()

ll.print_singly(head)
ll.display(head)  # 1 -> 2 -> 3 -> 4 -> 5
print(ll.search(head, 3))  # True
print(ll.search(head, 9))  # False


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(values: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        print("Adding value:", v)
        curr.next = ListNode(v)
        print("Current list:", end=" ")
        temp = dummy.next
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")
        curr = curr.next
    return dummy.next


print("Linked List built from list:", build([1, 2, 3, 4, 5]))
