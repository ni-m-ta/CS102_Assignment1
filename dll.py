class Node:
    
    # Initialization / Constructor -- specify variables for this object
    def __init__(self, x):
        self.__refNext = None # Reference to a potential next node, None by default
        self.__refPre = None # Reference to a potential previous node, None by default
        self.__value = x
    
    # Accessor methods
    # a.k.a getters and setters
    
    def getNext(self):
        return self.__refNext
        
    def setNext(self, r):
        self.__refNext = r

    def getPre(self):
        return self.__refPre

    def setPre(self, r):
        self.__refPre = r

    def getValue(self):
        return self.__value
        
    def setValue(self, x):
        self.__value = x

class DLL:
    
    # Initialization / Constructor -- specify variables for this object
    def __init__(self):
        self.__head = None # when we create the DLL we start it as an empty list
        self.__tail = None # add a tail reference to end of list
        
    # Accessor methods - getters and setters
    def getHead(self):
        return self.__head
        
    def setHead(self, h):
        self.__head = h
        
    # Methods to make the Singly Linked List work
    def add2Head(self, x):
        if self.__head == None:
            # add a new Node to the front of empty list
            newNode = Node(x)
            self.__head = newNode 
            self.__tail = newNode
            #self.setHead(Node(x))
        else: # add a new Node to the front of a list with existing Nodes
            newNode = Node(x)   # create the newNode
            preHeadNode = self.__head
            newNode.setNext(preHeadNode)
            preHeadNode.setPre(newNode)
            self.__head = newNode

    def add2Tail(self, x):
        if self.__head is None:
            self.add2Head(x)
        else:
            newNode = Node(x)
            preTailNode = self.__tail
            preTailNode.setNext(newNode)
            newNode.setPre(preTailNode)
            self.__tail = newNode

    def insert(self, pos, y):
        traverser = self.__head
        counter = 0
        while  counter < pos-1:
            traverser = traverser.getNext()
            counter += 1
        preNode = traverser
        if self.__head is None:
            self.add2Head(y)
        elif self.__tail == preNode:
            self.add2Tail(y)
        else:
            newNode = Node(y)
            newNode.setNext(preNode.getNext())
            newNode.setPre(preNode)
            preNode.setNext(newNode)

    def remove(self, x):
        if self.__head is None:
            print('It does not work')
        else:
            traverser = self.__head
            while traverser.getValue() != x:
                preNode = traverser
                traverser = traverser.getNext()
            nexNode = traverser.getNext()
            if x == self.__head.getValue():
                self.__head == nexNode
            elif x == self.__tail.getValue():
                self.__tail == preNode
            else:
                preNode.setNext(nexNode)
                nexNode.setPre(preNode)

    def display(self):
        # case: list is empty
        if self.__head is None:
            print("List is empty.")
        else: #case: list has elements
            print("->", end='')
            traverser = self.__head
            while traverser is not None:
                print(str(traverser.getValue())+"->", end='')
                traverser = traverser.getNext()
            print("||")
# # Test code
# '''
# newNode = Node(5)   # creation of the object -- is a call to the constructor or init method (line 11)

# print(newNode.getvalue())
# print(newNode.getNext())
# '''

d1 = DLL()  # Create a new Singly Linked List

d1.display()

d1.add2Head(3)
d1.add2Head(4)
d1.add2Tail(5)
d1.insert(2,10)
# d1.remove(4)
d1.display()
