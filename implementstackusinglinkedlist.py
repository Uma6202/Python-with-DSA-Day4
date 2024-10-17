# Define a Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer as None

# Define the Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Initialize the top of the stack as None

    def is_empty(self):
        return self.top is None  # Return True if stack is empty

    def push(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.top  # Set the new node's next pointer to current top
        self.top = new_node  # Update top to the new node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")  # If stack is empty, print underflow message
            return None
        popped_node = self.top  # Store the top node
        self.top = self.top.next  # Update top to the next node
        return popped_node.data  # Return the popped node's data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")  # If stack is empty, print empty message
            return None
        return self.top.data  # Return the data of the top node

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()  # Stack: 30 -> 20 -> 10 -> None

print("Top element:", stack.peek())  # Top element: 30
print("Popped element:", stack.pop())  # Popped element: 30
stack.display()  # Stack: 20 -> 10 -> None
