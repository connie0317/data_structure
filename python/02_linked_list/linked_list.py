

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
    def inserAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    
