class Node:
    # Node class to define each node in the doubly linked list
    def __init__(self, x):
        self.__refNext = None # Initialize the reference to the next node as None
        self.__refPre = None # Initialize the reference to the previous node as None
        self.__value = x # Initialize the value of the node as x


    def get_next(self):
        # Getter method to return the reference to the next node
        return self.__refNext

    def set_next(self, r):
        # Setter method to set the reference to the next node
        self.__refNext = r

    def get_pre(self):
        # Getter method to return the reference to the previous node
        return self.__refPre

    def set_pre(self, r):
        # Setter method to set the reference to the previous node
        self.__refPre = r

    # Getter method to return the value of the node
    def get_value(self):
        return self.__value

    def set_value(self, x):
        # Setter method to set the value of the node
        self.__value = x


class DLL:
    # Doubly linked list class

    def __init__(self):
        # Constructor to initialize the head and tail of the list as None
        self.__head = None 
        self.__tail = None

    def get_head(self):
        # Getter method to return the head node of the list
        return self.__head

    def get_tail(self):
        # Getter method to return the tail node of the list
        return self.__tail

    def set_head(self, h):
        # Setter method to set the head node of the list
        self.__head = h


    def add_to_head(self, x):
        # Method to add a new node to the head of the list
        if self.__head == None:
            # If the list is empty, create a new node and set it as both head and tail
            newNode = Node(x)
            self.__head = newNode 
            self.__tail = newNode
        else: 
            # If the list is not empty, create a new node and set it as the head
            newNode = Node(x)
            preHeadNode = self.__head
            newNode.set_next(preHeadNode)
            preHeadNode.set_pre(newNode)
            self.__head = newNode


    def add_to_tail(self, x):
        # Method to add a new node to the tail of the list
        if self.__head is None:
            # If the list is empty, add the node to the head
            self.add_to_head(x)
        else:
            # If the list is not empty, create a new node and set it as the tail
            newNode = Node(x)
            preTailNode = self.__tail
            preTailNode.set_next(newNode)
            newNode.set_pre(preTailNode)
            self.__tail = newNode


    def insert(self, pos, y):
        # Method to insert a new node at a specific position in the list
        traverser = self.__head
        counter = 0
        while  counter < pos-1:
            traverser = traverser.get_next()
            counter += 1
        preNode = traverser
        nexNode = traverser.get_next()
        if self.__head is None:
            self.add_to_head(y)
        elif self.__tail == preNode:
            self.add_to_tail(y)
        else:
            newNode = Node(y)
            nexNode.set_pre(newNode)
            newNode.set_next(nexNode)
            preNode.set_next(newNode)
            newNode.set_pre(preNode)


    def remove(self, x):
        # Method to remove a node with a specific value from the list
        if self.__head is None:
            print('List is empty')
        else:
            traverser = self.__head
            while traverser.get_value() != x:
                preNode = traverser
                traverser = traverser.get_next()
            nexNode = traverser.get_next()
            if x == self.__head.get_value():
                nexNode.set_pre(None)
                self.__head = nexNode
            elif x == self.__tail.get_value():
                preNode.set_next(None)
                self.__tail = preNode
            else:
                preNode.set_next(nexNode)
                nexNode.set_pre(preNode)

    def display(self):
        # Method to display the list of nodes
        if self.__head is None:
            print("List is empty.")
        else:
            print("Display: ->", end='')
            traverser = self.__head
            while traverser is not None:
                print(str(traverser.get_value())+"->", end='')
                traverser = traverser.get_next()
            print("||")


    def display_reversely(self):
        # Method to display the list of reversed nodes
        if self.__head is None:
            print("List is empty")
        else:
            print("Reversely display: ||<-", end="")
            traverser = self.__tail
            while traverser is not None:
                print(str(traverser.get_value())+"<-", end="")
                preNode =  traverser.get_pre()
                traverser = preNode
            print()
            print('----------------------------------------------------------------')


# Create a new doubly Linked List
dll = DLL()

# Test add_to_head() function
dll.add_to_head(1)
dll.add_to_head(2)
dll.add_to_head(3)
dll.display() # Expected output: ->3->2->1||
dll.display_reversely() # Expected output: ||<-1<-2<-3

# Test add_to_tail() function
dll.add_to_tail(4)
dll.add_to_tail(5)
dll.add_to_tail(6)
dll.display() # Expected output: ->3->2->1->4->5->6||
dll.display_reversely() # Expected output: ||<-6<-5<-4<-1<-2<-3

# Test insert() function
dll.insert(3, 7)
dll.display() # Expected output: ->3->2->1->7->4->5->6||
dll.display_reversely() # Expected output: ||<-6<-5<-4<-7<-1<-2<-3

# Test remove() function
dll.remove(4)
dll.display() # Expected output: ->3->2->1->7->5->6||
dll.display_reversely() # Expected output: ||<-6<-5<-7<-1<-2<-3

dll.remove(3)
dll.display() # Expected output: ->2->1->7->5->6||
dll.display_reversely() # Expected output: ||<-6<-5<-7<-1<-2

dll.remove(6)
dll.display() # Expected output: ->2->1->7->5||
dll.display_reversely() # Expected output: ||<-5<-7<-1<-2

# Test remove() function on empty list
dll2 = DLL()
dll2.remove(1) # Expected output: "List is empty."
