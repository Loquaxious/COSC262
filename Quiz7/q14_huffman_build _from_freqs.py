"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, April 2021.
"""
import re
from collections import defaultdict
import heapq

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root
        
    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        memo = defaultdict(str)
        split_text = list(text)
        return_str = ''
        
        trace_list = self.leaf_codes(self.root, '')
        for char in trace_list:
            memo[char[1]] = char[0]
        
        for letter in split_text:
            return_str += memo[letter]
        
        return return_str
        
    def leaf_codes(self, root, trace_str):
        """Recusively gathers the code to each char in the tree"""
        if root:
            if root.is_leaf():
                return [(trace_str, root.char)]
            else:
                result = []
                result.extend(self.leaf_codes(root.left, trace_str + '0'))
                result.extend(self.leaf_codes(root.right, trace_str + '1'))
                return result
        else:
            return []
            
    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        bin_code = list(binary)
        char_list = ''
        tree = self.root
        
        for char in bin_code:

            if char == '0':
                if tree.left.is_leaf():
                    char_list += tree.left.char
                    tree = self.root                   
                else:
                    tree = tree.left
            else:
                if tree.right.is_leaf():
                    char_list += tree.right.char
                    tree = self.root                    
                else:
                    tree = tree.right 
        
        return char_list

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        trees = []
        
        for key in freqs:
            trees.append(Leaf(freqs[key], key))
            
        trees.sort(key=lambda x : (x.count, x.min_char), reverse=True)
       
        while len(trees) > 1:
            left = trees.pop()
            right = trees.pop()
            trees.append(Node(left, right))
            trees.sort(key=lambda x : (x.count, x.min_char), reverse=True)

        
        self.root = trees[0]
            

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


def main():
    """ Demonstrate defining a Huffman tree from its string representation and
        printing and plotting it (if plotting is enabled on your machine).
    """
    # Example from Q11
    freqs = {
       'p': 27,
       'q': 11,
       'r': 27,
       'u': 8,
       't': 5,
       's': 3}
    tree = HuffmanTree()
    tree.build_from_freqs(freqs)
    print(tree)
    
main()