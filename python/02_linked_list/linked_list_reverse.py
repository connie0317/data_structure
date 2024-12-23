class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class LinkedList: 
    # Function to initialize head 
    def __init__(self): 
        self.head = None
    
    # Function to reverse the linked list 
    def reverse(self): 
        prev = None
        cur = self.head 
        while cur: 
            # 调换顺序之 把prev给next，把next先存tmp
            tmp = cur.next
            cur.next = prev 
            # 重新赋值, 向前滚动一格，cur变prev, tmp变cur
            prev = cur
            cur = tmp 
        self.head = prev 
    
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data,end=" ") 
            temp = temp.next
    
llist = LinkedList() 
llist.push(20) 
llist.push(4) 
llist.push(15) 
llist.push(85) 
  
print ("Given Linked List") 
llist.printList() 
llist.reverse() 
print ("\nReversed Linked List") 
llist.printList() 