class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return  temp.value

    def preappend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
    def get(self,index):
        if self.length == 0 or index >= self.length:
            return None
        temp = self.head
        i = 0
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.preappend(value)
        elif index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
my_linkedList = LinkedList(0)
my_linkedList.append(1)
my_linkedList.append(2)
my_linkedList.append(3)
#my_linkedList.print_list()
#my_linkedList.pop()
#my_linkedList.print_list()
#my_linkedList.preappend(1)
#my_linkedList.print_list()
#my_linkedList.pop_first()
#my_linkedList.print_list()
#print(my_linkedList.get(0))
#print(my_linkedList.get(1))
#print(my_linkedList.get(2))
#print(my_linkedList.get(3))
#print(my_linkedList.get(4))
my_linkedList.reverse()
print(my_linkedList.print_list())