class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingLinkList(object):
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    @property
    def is_empty(self):
        return self.__head == None

    @property
    def length(self):
        if self.is_empty:
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        if self.is_empty:
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=" ")
            cur = cur.next
        print(cur.item, end="\n")

    def add(self, item):
        node = Node(item)
        if self.is_empty:
            self.__head = node
            node.next = node
            return
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = self.__head