#Encoding : utf-8
"""This program can show a binary tree in simple format"""


class BinaryTree():
    """Class for creating a binary tree"""

    def __init__(self):
        """initiation"""
        self.root = None

    def print_tree(self):
        """Put the treee to the right format"""
        return self.root.display_node()

    def print_depth(self):
        """know the depth of the tree"""
        return self.root.number_of_nodes()


class Node():
    """Class for creating a node on Tree"""

    def __init__(self, value):
        """initiation"""
        self.value = value
        self.right = None
        self.left = None
        self.depth = 0

    def add(self, left=None, right=None):
        """add a node"""
        self.left = left
        self.right = right
        if self.left:
            left.depth = self.depth + 1
            left.update_children_depth()
        if self.right:
            right.depth = self.depth + 1
            right.update_children_depth()

    def update_children_depth(self):
        """update depth of tree"""
        if self.left:
            self.left.depth = self.depth + 1
            self.left.update_children_depth()
        if self.right:
            self.right.depth = self.depth + 1
            self.right.update_children_depth()

    def display_node(self):
        """Put the tree horizontally"""
        tabulation = ""
        for _ in range(0, self.depth):
            tabulation += "\t"
        result = tabulation + str(self) + "\n"
        if self.right:
            result += self.right.display_node()
        if self.left:
            result += self.left.display_node()
        return result

    def display_node_vertically(self):
        """Put the tree vertically"""
        depth = self.get_max_depth()
        indent = ""
        first_input = ""
        second_input = ""
        for _ in range(0, depth-2):
            indent += "\t"
            first_input = indent + str(self) + "\n"
        indent = ""
        if self.left is None and self.right is None:
            return self
        for _ in range(0, depth-2):
            indent += "\t"
            if self.right and self.left:
                second_input = indent + \
                    str(self.left.display_node_vertically()) + indent + \
                    str(self.right.display_node_vertically())
            elif self.left is None and self.right:
                second_input = indent + \
                    str(self.right.display_node_vertically())
            elif self.right is None and self.left:
                second_input = indent + \
                    str(self.left.display_node_vertically())
        final = first_input + second_input
        return final

    def __str__(self):
        """To have a D/V form"""
        return str(self.value) + "/" + str(self.depth)

    def is_leaf(self):
        """is this node is a leaf ?"""
        return not (self.left or self.right)

    def get_max_depth(self, max_depth=0):
        """To have the depth total of tree"""
        if self.is_leaf():
            if self.depth > max_depth:
                return self.depth
            return max_depth
        if self.right:
            max_depth = self.right.get_max_depth(max_depth)
        if self.left:
            max_depth = self.left.get_max_depth(max_depth)
        return max_depth

    def number_of_nodes(self, nodes=1):
        """Method to count the number of node"""
        if self.right:
            nodes = +1 + self.right.number_of_nodes(nodes)
        if self.left:
            nodes = +1 + self.left.number_of_nodes(nodes)
        return nodes


node1 = Node(0)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node3.add(node4)
node1.add(node2, node3)
tree1 = BinaryTree()
tree1.root = node1

node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node5.add(node6, node7)
node4.add(node5)
node8 = Node(8)
node7.add(node8)

print("==============NORMAL WAY==============")

print(tree1.print_tree())

print("==============VERTICAL WAY==============")

print(node1.display_node_vertically())

print("==============DEPTH==============")

print(tree1.print_depth())
