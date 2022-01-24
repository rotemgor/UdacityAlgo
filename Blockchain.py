import hashlib
import time


class Node:
    def __init__(self, my_block):
        self.value = my_block
        self.next = None


class Block:
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


class Blockchain:
    def __init__(self):
        self.head=None

    def append(self,data):
        current_time = time.gmtime(time.time())
        if self.head is None:
            self.head = Node(Block(current_time, data, 0))
            return
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node=temp_node.next

            temp_node.next=Block(current_time, data, temp_node.value.hash)










