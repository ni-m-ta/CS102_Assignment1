class Node:
    # Node class to define each node in the doubly linked list
    def __init__(self, x):
        self.__refNext = None # Initialize the reference to the next node as None
        self.__refPre = None # Initialize the reference to the previous node as None
        self.__value = x # Initialize the value of the node as x


    def getNext(self):
        # Getter method to return the reference to the next node
        return self.__refNext

    def setNext(self, r):
        # Setter method to set the reference to the next node
        self.__refNext = r

    def getPre(self):
        # Getter method to return the reference to the previous node
        return self.__refPre

    def setPre(self, r):
        # Setter method to set the reference to the previous node
        self.__refPre = r

    # Getter method to return the value of the node
    def getValue(self):
        return self.__value

    def setValue(self, x):
        # Setter method to set the value of the node
        self.__value = x


class DLL:
    # Doubly linked list class

    def __init__(self):
        # Constructor to initialize the head and tail of the list as None
        self.__head = None 
        self.__tail = None

    def getHead(self):
        # Getter method to return the head node of the list
        return self.__head

    def getTail(self):
        # Getter method to return the tail node of the list
        return self.__tail

    def setHead(self, h):
        # Setter method to set the head node of the list
        self.__head = h


    def add2Head(self, x):
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
            newNode.setNext(preHeadNode)
            preHeadNode.setPre(newNode)
            self.__head = newNode


    def add2Tail(self, x):
        # Method to add a new node to the tail of the list
        if self.__head is None:
            # If the list is empty, add the node to the head
            self.add2Head(x)
        else:
            # If the list is not empty, create a new node and set it as the tail
            newNode = Node(x)
            preTailNode = self.__tail
            preTailNode.setNext(newNode)
            newNode.setPre(preTailNode)
            self.__tail = newNode


    def insert(self, pos, y):
        # Method to insert a new node at a specific position in the list
        traverser = self.__head
        counter = 0
        while  counter < pos-1:
            traverser = traverser.getNext()
            counter += 1
        preNode = traverser
        nexNode = traverser.getNext()
        if self.__head is None:
            self.add2Head(y)
        elif self.__tail == preNode:
            self.add2Tail(y)
        else:
            newNode = Node(y)
            nexNode.setPre(newNode)
            newNode.setNext(nexNode)
            preNode.setNext(newNode)
            newNode.setPre(preNode)


    def remove(self, x):
        # Method to remove a node with a specific value from the list
        if self.__head is None:
            print('List is empty')
        else:
            traverser = self.__head
            while traverser.getValue() != x:
                preNode = traverser
                traverser = traverser.getNext()
            nexNode = traverser.getNext()
            if x == self.__head.getValue():
                nexNode.setPre(None)
                self.__head = nexNode
            elif x == self.__tail.getValue():
                preNode.setNext(None)
                self.__tail = preNode
            else:
                preNode.setNext(nexNode)
                nexNode.setPre(preNode)

    def display(self):
        # Method to display the list of nodes
        if self.__head is None:
            print("List is empty.")
        else:
            print("Display: ->", end='')
            traverser = self.__head
            while traverser is not None:
                print(str(traverser.getValue())+"->", end='')
                traverser = traverser.getNext()
            print("||")


    def displayReverse(self):
        # Method to display the list of reversed nodes
        if self.__head is None:
            print("List is empty")
        else:
            print("Reversely display: ||<-", end="")
            traverser = self.__tail
            while traverser is not None:
                print(str(traverser.getValue())+"<-", end="")
                preNode =  traverser.getPre()
                traverser = preNode
            print()
            print('----------------------------------------------------------------')


# Create a new doubly Linked List
dll = DLL()

# Test add2Head() function
dll.add2Head(1)
dll.add2Head(2)
dll.add2Head(3)
dll.display() # Expected output: ->3->2->1||
dll.displayReverse() # Expected output: ||<-1<-2<-3

# Test add2Tail() function
dll.add2Tail(4)
dll.add2Tail(5)
dll.add2Tail(6)
dll.display() # Expected output: ->3->2->1->4->5->6||
dll.displayReverse() # Expected output: ||<-6<-5<-4<-1<-2<-3

# Test insert() function
dll.insert(3, 7)
dll.display() # Expected output: ->3->2->1->7->4->5->6||
dll.displayReverse() # Expected output: ||<-6<-5<-4<-7<-1<-2<-3

# Test remove() function
dll.remove(4)
dll.display() # Expected output: ->3->2->1->7->5->6||
dll.displayReverse() # Expected output: ||<-6<-5<-7<-1<-2<-3

dll.remove(3)
dll.display() # Expected output: ->2->1->7->5->6||
dll.displayReverse() # Expected output: ||<-6<-5<-7<-1<-2

dll.remove(6)
dll.display() # Expected output: ->2->1->7->5||
dll.displayReverse() # Expected output: ||<-5<-7<-1<-2

# Test remove() function on empty list
dll2 = DLL()
dll2.remove(1) # Expected output: "List is empty."
