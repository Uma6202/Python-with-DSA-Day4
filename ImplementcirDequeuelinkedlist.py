# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Reference to the next node
        self.prev = None  # Reference to the previous node

# Define the Deque class using doubly linked list
class Deque:
    def __init__(self):
        self.front = None  # Initialize front of the deque as None
        self.rear = None   # Initialize rear of the deque as None

    def is_empty(self):
        return self.front is None  # Return True if deque is empty

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():  # If deque is empty, both front and rear point to the new node
            self.front = self.rear = new_node
        else:
            new_node.next = self.front  # New node points to the current front
            self.front.prev = new_node  # Current front's prev points to the new node
            self.front = new_node  # Update the front to the new node

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():  # If deque is empty, both front and rear point to the new node
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear  # New node's prev points to the current rear
            self.rear.next = new_node  # Current rear's next points to the new node
            self.rear = new_node  # Update the rear to the new node

    def remove_front(self):
        if self.is_empty():
            print("Deque Underflow from front")
            return None
        removed_data = self.front.data  # Store the front data
        self.front = self.front.next  # Move front to the next node
        if self.front is None:  # If deque is empty after removal
            self.rear = None
        else:
            self.front.prev = None  # Set the new front's prev to None
        return removed_data  # Return the removed data

    def remove_rear(self):
        if self.is_empty():
            print("Deque Underflow from rear")
            return None
        removed_data = self.rear.data  # Store the rear data
        self.rear = self.rear.prev  # Move rear to the previous node
        if self.rear is None:  # If deque is empty after removal
            self.front = None
        else:
            self.rear.next = None  # Set the new rear's next to None
        return removed_data  # Return the removed data

    def peek_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.front.data  # Return the data of the front node

    def peek_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.rear.data  # Return the data of the rear node

    def display(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            current = self.front
            while current:
                print(current.data, end=" <-> ")
                current = current.next
            print("None")

# Example usage
deque = Deque()
deque.add_rear(34)
deque.add_rear(25)
deque.add_front(7)

deque.display()  # Deque: 5 <-> 10 <-> 20 <-> None

print("Front element:", deque.peek_front())  # Front element: 5
print("Rear element:", deque.peek_rear())  # Rear element: 20

deque.remove_front()
deque.display()  # Deque: 10 <-> 20 <-> None

deque.remove_rear()
deque.display()  # Deque: 10 <-> None
