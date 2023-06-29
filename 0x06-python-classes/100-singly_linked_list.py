#!/usr/bin/python3

'''define class for a singly linked list'''


class Node:
    '''represent node for singly linked list'''

    def __init__(self, data, next_node=None):
        '''Nodde initialisation

        Args:
            data for a new node.
            next_node for a new node
        '''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''get node data'''
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''get or set the next node'''
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''represent singly linked list'''

    def __init__(self):
        '''initialised new singly linked list'''
        self.__head = None

    def sorted_insert(self, value):
        '''insert new nodde to the singly likned list

        the node inserted is at the correct order

        Args:
            data for a new node.
            next_node for a new node
        '''
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        '''define the print representattion of the Singly Linked List'''
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
