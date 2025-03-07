class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        # Initial insert (at head)
        if not self.head:
            self.head = new_node

        # Insert at the end
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

        # # Display as a list
        # elements = []
        # current = self.head

        # while current:
        #     elements.append(current.data)
        #     current = current.next

        # print(elements)

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return f"{key} found."
            current = current.next

        return f"{key} not found."

    def delete(self, key):
        current = self.head
        previous = None

        # Delete at head
        if current and current.data == key:
            self.head = current.next
            return f"{key} deleted at the head node"

        # Traverse to find the key
        while current and current.data != key:
            previous = current
            current = current.next

        # Delete at the end/ middle
        if current is not None:
            previous.next = current.next
            return f"{key} deleted."

        # Key not found
        return f"{key} not found."


linkedlist = LinkedList()

for i in [10, 20, 30, 40, 50]:
    linkedlist.insert(i)

linkedlist.display()

print(linkedlist.search(10))  # first
print(linkedlist.search(50))  # last
print(linkedlist.search(30))  # middle
print(linkedlist.search(90))  # not found


print(linkedlist.delete(10))  # first
print(linkedlist.delete(50))  # last
print(linkedlist.delete(30))  # middle
print(linkedlist.delete(90))  # not found

linkedlist.display()
