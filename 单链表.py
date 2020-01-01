class Node:
    """
    实现一个节点
    """
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleList:
    """
    单链表对象
    """
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        头部添加节点
        :param item:
        :return:
        """
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        """
        尾部添加节点
        :param item:
        :return:
        """
        node = Node(item)
        cur = self.head
        if not cur:  # 判断是否为空链表
            self.add(item)
        else:
            while cur.next:  # 依次便利到尾部节点，并添加节点
                cur = cur.next
            cur.next = node

    @property
    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        if self.head:
            return False
        else:
            return True

    @property
    def length(self):
        """
        获取链表长度
        :return:
        """
        cur = self.head
        n = 0
        if not cur:
            return n
        else:
            while cur.next:
                cur = cur.next
                n += 1
            return n

    def traversal(self):
        """
        遍历链表
        :return:
        """
        cur = self.head
        if not cur:
            print("None")
        else:
            while cur.next:
                print(cur.item)
                cur = cur.next
            print(cur.item)

    def insert(self, index, item):
        """
        插入节点
        :param item:
        :return:
        """
        if index == 0:
            self.add(item)
        elif index >= self.length:
            self.append(item)
        else:
            cur = self.head
            n = 1
            while cur.next:
                if n == index:
                    break
                cur = cur.next
                n += 1
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def delete(self, item):
        """
        删除节点
        :param item:
        :return:
        """
        if self.is_empty:
            raise ValueError("null")
        cur = self.head
        if cur.item == item:
            self.head = cur.next
        else:
            while cur.next:
                pre = cur
                cur = cur.next
                if cur.item == item:
                    pre.next = cur

    def search(self, item):
        """
        查找结点
        :param item:
        :return:
        """
        cur = self.head
        while None != cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    s = SingleList()
    # 头部添加节点
    s.add("s")
    s.traversal()
    # 判断是否为空
    print(s.is_empty)
    # 尾部添加节点
    s.append("d")
    s.traversal()
    # 插入节点
    s.insert(2, "f")
    s.traversal()
    # 查找节点
    print(s.search("d"))
    # 删除节点
    s.delete("f")
    s.traversal()
