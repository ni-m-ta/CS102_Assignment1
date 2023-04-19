class Node:
    def __init__(self, value):
        self.key = value
        self.right = None
        self.left = None
        self.parent = None

    def get_value(self):
        return self.key

    def set_value(self, value):
        self.key = value

class BST:
    def __init__(self):
        self.root = None
        self.left_leaf = None
        self.right_leaf = None

    def display(self, current_node):
        if current_node is not None:
            self.display(current_node.left)
            print(current_node.get_value(), end='->')
            self.display(current_node.right)
        return

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = Node(value)
            return
        current_node = self.root
        while current_node is not None:
            if current_node.get_value() > new_node.get_value():
                if current_node.left is None:
                    current_node.left = new_node
                    current_node = None
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    current_node = None
                else:
                    current_node = current_node.right

    def remove(self, value):
        parent = None
        current_node = self.root
        # Search for the node.
        while current_node is not None:
            if current_node.get_value() == value:
                if current_node.left is None and current_node.right is None: # the current node is leaf
                    if parent is None:
                        self.root = None
                    elif parent.left is current_node: 
                        parent.left = None
                    else:
                        parent.right = None
                    return
                elif current_node.left is not None and current_node.right is None: # the current node has a left child
                    if parent is None:
                        self.root = current_node.left
                    elif parent.left is current_node: 
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return
                elif current_node.left is None and current_node.right is not None: # the current node has a right child
                    if parent is None:
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return
                else:
                    # Find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.set_value(successor.get_value())
                    successor = None
            elif current_node.get_value() < value:
                parent = current_node
                current_node = current_node.right
            else:
                parent = current_node
                current_node = current_node.left
                
        return

    def search(self, value):
        if self.root is None:
            return self.root
        current_node = self.root
        while current_node is not None:
            if current_node.get_value() == value:
                return current_node
            elif current_node.get_value() < value:
                current_node = current_node.right
            elif current_node.get_value() > value:
                current_node = current_node.left
        return None


import unittest

class TestBinarySearchTree(unittest.TestCase):
    
    def setUp(self):
        self.bst = BST()
        
    def test_insert(self):
        print('Initial tree')
        self.bst.display(self.bst.root)

        self.bst.insert(50)
        self.assertEqual(self.bst.root.key, 50)
        self.assertIsNone(self.bst.root.left)
        self.assertIsNone(self.bst.root.right)
        
        self.bst.insert(30)
        self.assertEqual(self.bst.root.left.key, 30)
        self.assertIsNone(self.bst.root.left.left)
        self.assertIsNone(self.bst.root.left.right)
        
        self.bst.insert(20)
        self.assertEqual(self.bst.root.left.left.key, 20)
        self.assertIsNone(self.bst.root.left.left.left)
        self.assertIsNone(self.bst.root.left.left.right)
        
        self.bst.insert(40)
        self.assertEqual(self.bst.root.left.right.key, 40)
        self.assertIsNone(self.bst.root.left.right.left)
        self.assertIsNone(self.bst.root.left.right.right)
        
        self.bst.insert(70)
        self.assertEqual(self.bst.root.right.key, 70)
        self.assertIsNone(self.bst.root.right.left)
        self.assertIsNone(self.bst.root.right.right)
        
        self.bst.insert(60)
        self.assertEqual(self.bst.root.right.left.key, 60)
        self.assertIsNone(self.bst.root.right.left.left)
        self.assertIsNone(self.bst.root.right.left.right)
        
        self.bst.insert(80)
        self.assertEqual(self.bst.root.right.right.key, 80)
        self.assertIsNone(self.bst.root.right.right.left)
        self.assertIsNone(self.bst.root.right.right.right)

        print('\nFinal tree')
        self.bst.display(self.bst.root)

    def test_remove_case_1(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(70)
        self.bst.insert(60)
        self.bst.insert(80)

        print('\nInitial tree:')
        self.bst.display(self.bst.root)
        self.bst.remove(20)
        print('\nTree after removing node with key 20:')
        self.bst.display(self.bst.root)

        self.assertIsNone(self.bst.search(20))

    def test_remove_case_2_left(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(70)
        self.bst.insert(60)
        self.bst.insert(80)

        print('\nInitial tree:')
        self.bst.display(self.bst.root)
        self.bst.remove(30)
        # Display tree after removing node with key 30
        print('\nTree after removing node with key 30:')
        self.bst.display(self.bst.root)

        self.assertIsNone(self.bst.search(30))
        self.assertEqual(self.bst.search(20).key, 20)
        self.assertEqual(self.bst.search(40).key, 40)

    def test_remove_case_2_right(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(70)
        self.bst.insert(60)
        self.bst.insert(80)

        print('\nInitial tree:')
        self.bst.display(self.bst.root)
        self.bst.remove(70)
        # Display tree after removing node with key 70
        print('\nTree after removing node with key 70:')
        self.bst.display(self.bst.root)

        self.assertIsNone(self.bst.search(70))
        self.assertEqual(self.bst.search(60).key, 60)
        self.assertEqual(self.bst.search(80).key, 80)

    def test_remove_case_3(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(70)
        self.bst.insert(60)
        self.bst.insert(80)
        
        print('\nInitial tree:')
        self.bst.display(self.bst.root)
        self.bst.remove(30)
        # Display tree after removing node with key 30
        print('\nTree after removing node with key 30:')
        self.bst.display(self.bst.root)

        self.assertIsNone(self.bst.search(30))
        self.assertEqual(self.bst.search(20).key, 20)
        self.assertEqual(self.bst.search(40).key, 40)
        self.assertEqual(self.bst.search(50).key, 50)
        self.assertEqual(self.bst.search(60).key, 60)
        self.assertEqual(self.bst.search(70).key, 70)
        self.assertEqual(self.bst.search(80).key, 80)

if __name__ == '__main__':
    unittest.main()