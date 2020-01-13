# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''

        hash_a = 5381
        key_str_bytes = str.encode(key)
        for x in key_str_bytes:
            hash_a = ((hash_a << 5) + hash_a) + x
        
        return self._hash_mod(hash_a)


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # print('count: ', self.count)
        # print('capacity: ', self.capacity)
        # print('count/cap: ', self.count/self.capacity)
        # print('key, val', key, value)
        # print('-------------')

        # h = self._hash_mod(key)
        h = self._hash_djb2(key)

        if self.storage[h]:
            node = self.storage[h]
            while node:
                if node.key == key:
                    node.value = value
                    break
                elif node.next:
                    node = node.next
                else: 
                    node.next = LinkedPair(key, value)
                    self.count += 1
                    self.auto_size()
                    break
        
        else:
            self.storage[h] = LinkedPair(key, value)
            self.count += 1
            self.auto_size()

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # h = self._hash_mod(key)
        h = self._hash_djb2(key)

        if not self.storage[h]:
            print("WARNING! No such key found")
            return
        
        node = self.storage[h]
        while node:
            if node.key == key:
                temp = node.value
                node.value = None
                self.count -= 1
                self.auto_size()
                return temp
            elif node.next:
                node = node.next
            else:
                print("WARNING! No such key found")
                return

        pass


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # h = self._hash_mod(key)
        h = self._hash_djb2(key)

        if not self.storage[h]:
            return None
        else:
            node = self.storage[h]
            while node:
                if node.key == key:
                    return node.value
                node = node.next
            return None

        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        temp_list = []
        for a in self.storage:
            node = a
            while node:
                temp_list.append([node.key, node.value])
                node = node.next

        self.capacity = 2*self.capacity
        self.storage = [None]*self.capacity
        
        for b in temp_list:
            self.insert(b[0], b[1])
            self.count -= 1

    def shrink(self):
        temp_list = []
        for a in self.storage:
            node = a
            while node:
                temp_list.append([node.key, node.value])
                node = node.next

        self.capacity = self.capacity//2
        self.storage = [None]*self.capacity
        

        for b in temp_list:
            self.insert(b[0], b[1])
            self.count -= 1

    def auto_size(self):
        if self.count / self.capacity > 0.7:
            return self.resize()
        elif self.count / self.capacity < 0.2:
            return self.shrink()
        # pass
            
if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
