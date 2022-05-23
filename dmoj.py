class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

node_1 = Node("Once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time.")
node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

def insertNodeAtTail(head, data):
    new_head = head
    while head != None:
        head = head.next_node
    new_head = head
    head = Node(data)
    return head

class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def read(self,index):
        self.current_node = self.first_node
        self.current_index = 0

        while self.current_index < index:
            if self.current_node != None:
                self.current_node = self.current_node.next_node
                self.current_index+=1
            else:
                return None
        return self.current_node.data

    def index_of(self, value):
        self.current_node = self.first_node
        self.current_index = 0

        while True:
            if self.current_node.data == value:
                return self.current_index
            self.current_node = self.current_node.next_node
            self.current_index+=1
            if self.current_node == None:
                return None
        
linkedlist=LinkedList(node_1)
print(insertNodeAtTail(node_1, "WOW").data)
            
            
            
