import sys

class HuffmannTreeNode():
    def __init__(self,mychar,freq,left_child=None,right_child=None):
        self.char=mychar
        self.freq=freq
        self.left_child=left_child
        self.right_child=right_child
# add reference to
class PQ:
  def __init__(self):
    self.tree = BinaryTree()
    self.N = 0

  def __len__(self):
    return self.N

  def is_empty(self):
    return self.N == 0

  def is_full(self):
    return False

  def enqueue(self, v, p):
    self.tree.insert(v, p)
    self.N += 1

def huffman_encoding(data):
    for my_char in data:


def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))