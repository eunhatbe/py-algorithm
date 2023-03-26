
class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = None

    def add_data(self, data):
        new_node = Node(data=data)

        if not self.tail:
            self.tail = new_node
            self.head.set_next(new_node)
            return

        self.tail.set_next(new_node)
        self.tail = new_node

    def get_data_all(self):
        temp = self.head.get_next()

        while True:
            print(temp.get_data())

            if not temp.get_next():
                return

            temp = temp.get_next()

class Node:
    def __init__(self, next_addr=None, data=None):
        self.__next = next_addr
        self.__data = data

    def get_next(self):
        return self.__next

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def set_next(self, addr):
        self.__next = addr


my_list = LinkedList()

my_list.add_data(2)
my_list.add_data(3)
my_list.add_data(4)
my_list.add_data(5)

print(my_list.head.get_next().get_data())
print(my_list.head.get_next().get_next().get_data())
print(my_list.head.get_next().get_next().get_next().get_data())

my_list.get_data_all()

