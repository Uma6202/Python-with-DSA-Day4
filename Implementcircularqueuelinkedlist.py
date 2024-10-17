class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size  # Initialize the queue with None
        self.front = -1  # Initialize front pointer
        self.rear = -1   # Initialize rear pointer

    def is_empty(self):
        return self.front == -1  # Queue is empty when front is -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front  # Full condition for circular queue

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full, cannot enqueue")
            return
        if self.is_empty():
            self.front = 0  # Set front to 0 if the queue was empty
        self.rear = (self.rear + 1) % self.size  # Move rear in a circular manner
        self.queue[self.rear] = data  # Insert the data
        print(f"Enqueued {data} to the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        data = self.queue[self.front]  # Get the front data
        if self.front == self.rear:  # If there's only one element
            self.front = self.rear = -1  # Reset the queue after dequeueing
        else:
            self.front = (self.front + 1) % self.size  # Move front in a circular manner
        print(f"Dequeued {data} from the queue.")
        return data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]  # Return the front element

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements are:", end=" ")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()

# Example usage
cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)

cq.display()  # Queue: 10 20 30 40 50

cq.dequeue()
cq.dequeue()

cq.display()  # Queue: 30 40 50

cq.enqueue(60)
cq.enqueue(70)

cq.display()  # Queue: 30 40 50 60 70

print("Front element:", cq.peek())  # Front element: 30
