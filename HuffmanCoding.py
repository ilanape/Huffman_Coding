from collections import Counter
from queue import PriorityQueue
from TreeNode import TreeNode


class HuffmanCoding:
    def __init__(self, table=None):
        self.table = table

    def compress(self):
        # input file parsing
        try:
            input_file = open("Input Text File", "r")
            text_file = input_file.read()
        except IOError:
            print('"Input Text File" does not exist')
            input_file.close()

        # compute frequencies
        freq = Counter(text_file)

        # create tree nodes
        # nodes are sorted by freq. increasing order using priority queue
        queue = PriorityQueue()
        for letter, f in freq.items():
            queue.put(TreeNode(letter, f))

        # create Huffman tree using the priority queue
        while queue.qsize() > 1:
            # two smallest freq. nodes
            left = queue.get()
            right = queue.get()
            # new internal node
            queue.put(TreeNode(None, left.freq + right.freq, left, right))

        # create Huffman code table
        self.table = self.huffman_code(queue.get())

        # output files creation
        length = 0
        compressed_version = open("Compressed version", "w")
        compressed_length = open("Compressed length", "w")

        for letter in text_file:
            compressed_version.write(self.table[letter])
            length += len(self.table[letter])

        compressed_length.write(str(length))
        compressed_version.close()
        compressed_length.close()

    def huffman_code(self, node, binary_string=""):
        d = dict()
        # leaf node
        if node.has_children() is False:
            return {node.get_letter(): binary_string}

        # internal node - build recursively
        left, right = node.get_children()
        d.update(self.huffman_code(left, binary_string + '0'))
        d.update(self.huffman_code(right, binary_string + '1'))
        return d

    def decompress(self):
        # input file parsing
        try:
            input_file = open("Compressed version", "r")
            encoded_text = input_file.read()
        except IOError:
            print('"Compressed version" does not exist')
            input_file.close()

        # output file creation
        decoded_text = open("Decoded Text", "w")
        code = ""
        for bit in encoded_text:
            code += bit
            # code is in table
            if code in self.table.values():
                decoded_text.write(self.get_key(code))
                code = ""

        decoded_text.close()

    def get_key(self, code):
        for key, val in self.table.items():
            if code == val:
                return key

    def compare(self):


if __name__ == "__main__":
    # if sys.argv[1] == 'compress':
    #     compress()
    # elif sys.argv[1] == 'decompress':
    #     decompress()
    # elif sys.argv[1] == 'compare':
    #     compare()
    # else:
    #     print('Invalid format: HuffmanCoding.py [compress/decompress/compare]')

    huffmanInstance = HuffmanCoding()
    huffmanInstance.compress()
    huffmanInstance.decompress()