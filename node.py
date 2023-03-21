# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:34:37 2023

@author: crazy
"""

class Node:
    
    # Initialization / Constructor -- specify variables for this object
    def __init__(self, x):
        self.__refNext = None    # Reference to a potential next node, None by default
        self.__value = x
    
    # Accessor methods
    # a.k.a getters and setters
    
    def getNext(self):
        return self.__refNext
        
    def setNext(self, r):
        self.__refNext = r
        
    def getValue(self):
        return self.__value
        
    def setValue(self, x):
        self.__value = x
        
        
class SLL:
    
    # Initialization / Constructor -- specify variables for this object
    def __init__(self):
        self.__head = None # when we create the SLL we start it as an empty list
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
            newNode.setNext(self.__head)
            self.__head = newNode
            
    def add2Tail(self, x):
        if self.__head is None:
            self.add2Head(x)
        else:
            newNode = Node(x)
            self.__tail.setNext(newNode)
            self.__tail = self.__tail.getNext()


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
# Test code
'''
newNode = Node(5)   # creation of the object -- is a call to the constructor or init method (line 11)

print(newNode.getvalue())
print(newNode.getNext())
'''

s1 = SLL()  # Create a new Singly Linked List

s1.display()

# first add
s1.add2Head(19)
#print(s1.getHead().getNext())
#print(s1.getHead().getValue())

# second head
s1.add2Head(75)
#print(s1.getHead().getValue())
#print(s1.getHead().getNext().getValue())
s1.display()

s1.add2Head(23)
s1.add2Head(111)
s1.display()

s1.add2Tail(65)
s1.display()

s1.add2Tail(654)
s1.display()