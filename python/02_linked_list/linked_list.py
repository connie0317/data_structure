

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        # head is a node, check if the head is an empty node 
        if self.head is None:
            self.head = new_node
            return
        else:
            # new node becomes head and head becomes second node
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        # move to the node I want to do insertation, start from position 0
        # 假设我现在的position是0， 把屁股挪到要insert的node的前一个
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next
        # 挪到想去的node之后
        # 如果node是none，没有数据可以加， 超出的链表的范围
        # 如果node不是none，可以创建一个新的node
        # 新的node的data就是我要加的数值，修改next即可
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # 先建new node
    # check if head is none
    # else 挪屁股直到下一个node是none
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node


    def updateNode(self, val, index):
        current_node = self.head 
        position = 0 
        if position == index:
            current_node.data = val 
        else: 
            while (current_node != None and position != index):
                position += 1
                current_node = current_node.next 
            if current_node != None:
                current_node.data = val 
            else:
                print("Index not present")


    def remove_first_node(self):
        # if nothing to remove 
        if(self.head == None):
            return
        # remove head, replace head with head next 
        self.head = self.head.next


    def remove_last_node(self):
        # if head is None 
        if self.head is None:
            return

        curr_node = self.head
        while (curr_node.next != None and curr_node.next.next != None):
            curr_node = curr_node.next

        curr_node.next = None


    # Method to remove at given index
    def remove_at_index(self, index):
        # 如果链表是空的，则什么都不做
        if self.head is None:
            return

        current_node = self.head
        position = 0 
        # 如果指定删除的Node节点是链表的头节点
        if index == 0:
            self.remove_first_node()

        else:
            while current_node.next != None: 
                
                if position + 1 == index: 
                    current_node.next = current_node.next.next 
                    return 
                else: 
                    position += 1
                    current_node = current_node.next 
                
            if index > position:
                print("index not present")
                return  

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next


    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
    
# create a new linked list
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)

# print the linked list
print("Node Data:")
llist.printLL()

# check username change