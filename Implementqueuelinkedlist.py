# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer as None

# Define the Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None  # Initialize front of the queue as None
        self.rear = None   # Initialize rear of the queue as None

    def is_empty(self):
        return self.front is None  # Return True if queue is empty

    def enqueue(self, data):
        new_node = Node(data)  # Create a new node
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node  # Both front and rear point to the new node
        else:
            self.rear.next = new_node  # Attach the new node at the rear
            self.rear = new_node  # Update the rear to the new node

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")  # If queue is empty, print underflow message
            return None
        temp = self.front  # Store the current front node
        self.front = self.front.next  # Move the front to the next node
        if self.front is None:  # If the front becomes None, then the queue is empty
            self.rear = None  # Update rear to None
        return temp.data  # Return the dequeued node's data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")  # If queue is empty, print empty message
            return None
        return self.front.data  # Return the data of the front node

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()  # Queue: 10 -> 20 -> 30 -> None

print("Front element:", queue.peek())  # Front element: 10
print("Dequeued element:", queue.dequeue())  # Dequeued element: 10
queue.display()  # Queue: 20 -> 30 -> None
