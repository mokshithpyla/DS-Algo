"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        pos = 1
        current = self.head
        if position < 1:
            return None
        while current and pos <= position:
            if pos == position:
                return current
            current = current.next
            pos += 1
        return None

    def insert(self, new_element, position):
        pos = 1
        current = self.head
        if position > 1:
            while current and pos < position:
                if pos == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                pos += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# print ll.get_position(3).value
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)