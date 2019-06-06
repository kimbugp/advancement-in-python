class Node(object):
    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data

    def __repr__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self, head=None):
        if head is not None:
            assert isinstance(head, Node), 'Head must be a node object'
        self.head = head

    def __len__(self):
        cursor = self.head
        counter = 0
        while cursor is not None:
            counter += 1
            cursor = cursor.next
        return counter

    def __str__(self):
        return self.head

    def push(self, data=None):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def __repr__(self):
        data = []
        cursor = self.head
        while cursor is not None:
            data.append(cursor.data)
            cursor = cursor.next
        return str(data)
