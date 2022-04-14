class Node(object):
    def __init__(self, value,next=None):
        self.value = value
        self.next = next

#Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
def has_cycle(head):

    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        print("fast",fast.value)
        print("slow",slow.value)
        if slow == fast:
            return True
    return False

#Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
def find_cycle(head):
    cycle_length = 0
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            print("slow",slow.value)
            cycle_length = find_cycle_length(slow)
            break
    return cycle_start(head,cycle_length)

def find_cycle_length(slow):
    cycle_length = 0
    current = slow
    while True:
        current= current.next
        cycle_length +=1
        if current == slow:
            break
    print(cycle_length)
    return cycle_length

def cycle_start(head,cycle_length):
    ptr1,ptr2 = head,head
    while cycle_length > 0:
        ptr2 = ptr2.next
        cycle_length-=1

    while ptr1!= ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1

#Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’.
#For example 23 is a happy number since 4 + 9 = 13 -> 1 + 9 = 10 -> 1+ 0 = 1

def happy_number(num):
    slow,fast = num,num
    while True:
        slow = find_sum(slow)
        fast = find_sum(find_sum(fast))
        print("f",fast)
        print("s",slow)
        if slow==fast:
            break
    return slow == 1

def find_sum(num):
    _sum = 0
    while num >0:
        digit = num%10
        _sum += digit **2
        num = num//10
    return _sum

#Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
#If the total number of nodes in the LinkedList is even, return the second middle node.
def find_middle(head):
    slow,fast = head,head
    while fast is not None and fast.next is not None:
        slow= slow.next
        fast = fast.next.next
    return slow

#Write a method to determine if the array has a cycle.
# The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements

def circular_array_loop_exists(arr): #[1,1,2]
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow,fast = i,i

        while True:
            slow = find_next_index(arr,is_forward,slow)
            fast = find_next_index(arr,is_forward,fast)
            if fast !=-1:
                fast = find_next_index(arr, is_forward, fast)

            if slow == fast or slow== -1 or fast == -1:
                break
        if slow !=-1 and slow==fast:
            return True
    return False

def find_next_index(arr,is_forward,current):
    direction = arr[current] >=0
    if direction != is_forward:
        return -1

    next_index = (current + arr[current]) % len(arr)
    if next_index == current:
        next_index = -1

    return next_index

#Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
def palindrome(head):
    arr = []
    ptr = head
    while ptr is not None :
        arr.append(ptr.value)
        ptr = ptr.next
    return arr == arr[::-1]

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    #head.next.next.next.next.next = Node(6)

    #head.next.next.next.next.next.next = head.next
    #print("LinkedList has cycle: "+str(has_cycle(head)))
    print("Linked has cycle at position: ",find_cycle(head).value)

    print("Is this number happy: ",happy_number(23))
    print("Is this number happy: ",happy_number(12))

    print("Middle of number is: ",find_middle(head).value)
    print("Array has Circular Loop : ",circular_array_loop_exists([-1,-1,-1]))
    print("Linked List is Palindrome: ",palindrome(head))

main()