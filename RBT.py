class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.null_node = Node(None)
        self.null_node.color = 0
        self.null_node.left = None
        self.null_node.right = None
        self.root = self.null_node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def fix_insert(self, z):
        while z.parent.color == 1:
            if z.parent == z.parent.parent.right:
                u = z.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.left_rotate(z.parent.parent)
            else:
                u = z.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 0
                    z.parent.parent.color = 1
                    self.right_rotate(z.parent.parent)
            if z == self.root:
                break

        self.root.color = 0

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        y = None
        x = self.root

        while x != self.null_node:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def search(self, key):
        """
        Метод для поиска узла с заданным ключом в дереве.
        Возвращает найденный узел или None, если узел не найден.
        """
        x = self.root
        while x != self.null_node and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if x == self.null_node:
            return False
        else:
            return True

    def inorder_traversal(self, node):
        if node != self.null_node:
            self.inorder_traversal(node.left)
            print(node.key)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node != self.null_node:
            print(node.key)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node != self.null_node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key)

    def inorder(self):
        """
        Метод для прямого обхода дерева.
        """
        self.inorder_traversal(self.root)

    def preorder(self):
        """
        Метод для центрального обхода дерева.
        """
        self.preorder_traversal(self.root)

    def postorder(self):
        """
        Метод для обратного обхода дерева.
        """
        self.postorder_traversal(self.root)

    def delete(self, key):
        node = self.root
        while node != self.null_node and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if node == self.null_node:
            raise ValueError("Node not found")

        if node.left == self.null_node or node.right == self.null_node:
            y = node
        else:
            y = self.successor(node)

        if y.left != self.null_node:
            x = y.left
        else:
            x = y.right

        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        if y != node:
            node.key = y.key

        if y.color == 0:
            self.fix_delete(x)

    def fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 0 and w.right.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.right.color == 0:
                        w.left.color = 0
                        w.color = 1
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 0 and w.left.color == 0:
                    w.color = 1
                    x = x.parent
                else:
                    if w.left.color == 0:
                        w.right.color = 0
                        w.color = 1
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def successor(self, node):
        if node.right != self.null_node:
            return self.minimum(node.right)
        y = node.parent
        while y != self.null_node and node == y.right:
            node = y
            y = y.parent
        return y

    def minimum(self, node):
        while node.left != self.null_node:
            node = node.left
        return node


tree = RedBlackTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(15)
tree.insert(25)

print(tree.search(15))
print(tree.search(40))

print("Inorder traversal:")
tree.inorder()

print("Preorder traversal:")
tree.preorder()

print("Postorder traversal:")
tree.postorder()

print('before del')
tree.inorder()
tree.delete(20)
print('after del')
tree.inorder()
