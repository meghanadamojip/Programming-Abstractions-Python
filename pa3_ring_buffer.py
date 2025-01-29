class RingBuffer:
    def __init__(self, a: int):  # defining variables
        self.a = a  # size of queue
        self.b = []  # empty list to store the data in

    def en_queue(self, value: int):
        if len(self.b) == self.a:  # check if queue is full
            self.b.pop(-1)  # remove the tail value if queue is full
        self.b.insert(0, value)  # insert value and shift everything else to the right

    def de_queue(self) -> bool:  # define function to delete item at the front of the queue
        if len(self.b) > 0:  # remove the next in line if queue is not empty
            self.b.pop(-1)  # remove the item at the given index from the list
            return True  # return true
        else:
            return False  # else return false

    def get_front(self) -> int:  # returns the front item from the queue. Returns -1 if the queue is empty.
        if len(self.b) > 0:  # if length of queue is greater than 0
            return self.b[-1]
        else:
            return -1

    def get_rear(self) -> int:  # Returns the last item from the queue. Returns -1 if the queue is empty.
        if len(self.b) == 0:
            return -1
        else:
            return self.b[0]

    def is_empty(self) -> bool:  # Returns true if the queue is empty, or false otherwise.
        if len(self.b) == 0:
            return True
        else:
            return False

    def is_full(self):  # Returns true if the queue is full, or false otherwise.
        if len(self.b) == self.a:
            return True
        else:
            return False

    def get_average(self) -> float:  # Returns average of numbers in the ring buffer; if it is empty, returns None
        if len(self.b) == 0:
            return None
        count = 0  # getting result of each component in the list added and then dividing by the number of components
        for i in self.b:  # for loop
            count += i  # add to i
        return count / len(self.b)  # return the average

