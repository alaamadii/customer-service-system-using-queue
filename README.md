## Customer Service Queue Simulator (Python)

This project simulates a **basic customer service system** using a **queue** implemented in Python without using any built-in queue libraries.  
Customers arrive, join the queue, and are served in the order they arrive (FIFO: First-In-First-Out).

---

##  Features
- Simulates customer arrivals.
- Enqueues and dequeues customers in order.
- Displays the name of each customer as they are served.
- Prints a message when all customers have been served.
- Uses a **custom queue implementation** without built-in queue functions.

---

##  Example Usage

### Input / Simulation
```python
customers = ["Alice", "Bob", "Carol"]

Output
Arriving: Alice
Arriving: Bob
Arriving: Carol
Serving: Alice
Serving: Bob
Serving: Carol
All customers served
