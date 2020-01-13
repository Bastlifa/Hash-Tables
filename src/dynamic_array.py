class DynamicArray:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count == self.capacity:
            # TODO: resize
            print('Error: array is full')
            return
        else:
            #  Shift to the right
            for i in range(self.count, index, -1):
                self.storage[i] = self.storage[i-1]

            self.storage[index] = value
            self.count += 1

    def append(self, value):
        self.insert(self.count + 1, value)

    def resize(self):
        self.capacity *=2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        
        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
        self.insert(0, value)

    def slice_arr(self, beginning_index, end_index):
        # beginning and end
        # subarray
        # copy beginning to end to subarray
        # remove from array
        # return subarray
