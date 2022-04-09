class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


def main():

    link_list = LinkedList()

    node1 = Node("2")
    link_list.head = node1
    
    node2 = Node("5")
    node1.next = node2
    
    node3 = Node("7")
    node2.next = node3

    #print(link_list)
    print(int(11% 10))

if __name__ == '__main__':
    main()

