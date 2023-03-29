'''
This file implements the AVL Tree data structure.
The functions in this file are considerably
harder than the functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__(xs)

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies
        that all nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if node:
            if AVLTree._balance_factor(node) in [-1, 0, 1]:
                ret &= AVLTree._is_avl_satisfied(node.left)
                ret &= AVLTree._is_avl_satisfied(node.right)
            else:
                ret = False
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly
        different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        left_height = BinaryTree._height(node.left)
        right_height = BinaryTree._height(node.right)
        node.height = max(left_height, right_height) + 1
        left_height = BinaryTree._height(new_root.left)
        right_height = BinaryTree._height(new_root.right)
        new_root.height = max(left_height, right_height) + 1
        return new_root

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        left_height = BinaryTree._height(node.left)
        right_height = BinaryTree._height(node.right)
        node.height = max(left_height, right_height) + 1
        left_height = BinaryTree._height(new_root.left)
        right_height = BinaryTree._height(new_root.right)
        new_root.height = max(left_height, right_height) + 1
        return new_root

    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of
        how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree
        code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar
        to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        def _insert(node, value):
            if node is None:
                return Node(value)
            elif value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            left_height = BinaryTree._height(node.left)
            right_height = BinaryTree._height(node.right)
            node.height = max(left_height, right_height) + 1
            balance_factor = AVLTree._balance_factor(node)
            if balance_factor > 1:
                if AVLTree._balance_factor(node.left) < 0:
                    node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            elif balance_factor < -1:
                if AVLTree._balance_factor(node.right) > 0:
                    node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            return node

        self.root = _insert(self.root, value)

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        bff = AVLTree._balance_factor(node)
        if bff == 2:
            if AVLTree._balance_factor(node.left) < 0:
                node.left = AVLTree._left_rotate(node.left)
            node = AVLTree._right_rotate(node)
        elif bff == -2:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
            node = AVLTree._left_rotate(node)
        return node
