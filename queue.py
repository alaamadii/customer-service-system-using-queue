class CustomerQueue:
    def __init__(self):
        self.items = []  

    def enqueue(self, customer):
        self.items.append(customer)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None


    def is_empty(self):
        return len(self.items) == 0

queue = CustomerQueue()


customers = ["Alice", "Bob", "Carol"]
for customer in customers:
    print(f"Arriving: {customer}")
    queue.enqueue(customer)

while not queue.is_empty():
    served = queue.dequeue()
    print(f"Serving: {served}")

print("All customers served.")