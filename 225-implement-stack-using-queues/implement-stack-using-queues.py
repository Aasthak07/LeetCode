class MyStack:

    def __init__(self):
        # q1 = main queue (will always keep the top element at the front)
        # q2 = helper queue (used for rearranging elements)
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        # APPROACH (Push-heavy):
        # 1. Move all elements from q1 → q2
        # 2. Insert new element into q1
        # 3. Move all elements back from q2 → q1
        #
        # INTUITION:
        # In a stack, the last inserted element should be on top.
        # To simulate this using queues (FIFO), we place the new element
        # at the front by temporarily removing all previous elements.

        while len(self.q1) > 0:
            self.q2.append(self.q1.pop(0))

        # Insert new element (this should become the top)
        self.q1.append(x)

        # Move back the previous elements
        while len(self.q2) > 0:
            self.q1.append(self.q2.pop(0))
        

    def pop(self) -> int:
        # APPROACH:
        # The top element is always at the front of q1,
        # so we can directly remove it.
        #
        # INTUITION:
        # Since we already arranged elements during push,
        # pop becomes very simple (O(1)).

        x = self.q1[0]
        self.q1.pop(0)
        return x
        

    def top(self) -> int:
        # The front of q1 is always the top of the stack
        return self.q1[0]
        

    def empty(self) -> bool:
        # Check if the stack is empty
        return len(self.q1) == 0