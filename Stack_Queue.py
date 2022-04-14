class Stack(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def pop(self):
        return self.items.pop()
    def push(self,el):
        self.items.append(el)
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.size())

class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        print("empty qeuue?",self.items == [])
    def enqueue(self,el):
        self.items.insert(0,el)
    def dequeue(self):
        print("deque",self.items.pop())
    def peek(self):
        print("peek queue",self.items[0])
    def size(self):
        print("size of queue",len(self.items))

q = Queue()
q.enqueue(1)
q.enqueue("two")
q.size()
q.dequeue()
q.peek()
