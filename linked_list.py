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
        self.validate_head(head)
        self.head = head

    def __len__(self):
        cursor = self.head
        counter = 0
        while cursor:
            counter += 1
            cursor = cursor.next
        return counter

    def validate_head(self, head):
        if head:
            assert isinstance(head, Node), 'Head must be a node object'

    def __str__(self):
        return self.head

    def push(self, data=None):
        if not data:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def __repr__(self):
        data = []
        cursor = self.head
        while cursor:
            data.append(cursor.data)
            cursor = cursor.next
        return str(data)
