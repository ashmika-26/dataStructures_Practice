# Check for cycle in linked List

class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.nextnode
        print()

def find_key(head,key):
    while head:
        if head.value == key:
            return "YES"
        head = head.nextnode
    return "No"


def mergeLists(headA, headB):

    head_node = Node(0)
    current = head_node
    while headA != None and headB != None:
        if headA.value <= headB.value:
            current.nextnode = headA
            headA = headA.nextnode
        else:
            current.next = headB
            headB = headB.nextnode

        current = current.nextnode

    current.next = headA if headB is None else headB

    return head_node.nextnode


def cycle_check(node):

    marker1,marker2 = node,node

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker1 == marker2:
            return "Cycle exists"

    return "No cycle"


def reverse(head):

    current = head
    previous = None
    next = None
    while current:
        next = current.nextnode
        current.nextnode = previous
        previous = current
        current = next
    return previous

def nth_to_last(head,n):
    left_pointer = right_pointer = head

    for _ in range(n-1):
       if not right_pointer.nextnode:
           raise LookupError("Error: n is larger than the linked list")
       right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer.value

def reverselist(head,k):
    current = head
    previous = None
    while k:
        next = current.nextnode
        current.nextnode = previous
        previous = current
        current = next
        k-=1
    return previous

def reverseKgroups(head,k):
    count,ptr = 0,head
    while count < k and ptr:
        count+=1
        ptr = ptr.nextnode
    if count == k:
        reversehead = reverselist(head,k)

        head.next = reverseKgroups(ptr,k)
        return reversehead
    return head

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    a.print_list()
    print(cycle_check(a))
    #result = reverse(a)
    #print(find_key(a,2))

    # x =Node(4)
    # y = Node(2)
    # z = Node (1)
    # a.nextnode = b
    # b.nextnode = c
    # c.nextnode = d
    # x.netnode = y
    # y.nextnode = z
    #
    #

    #
    # #print(d.nextnode.valu=-==-0=p=p=[==p=[[=[[[p]][[[]pp;llpllllll;lll;['[
    print("nth to last",nth_to_last(a,2))
    # # print(mergeLists(a,x))
    # rev = reverseKgroups(a,2)
    # rev.print_list()
main()

