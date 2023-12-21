class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = capacity *[None]