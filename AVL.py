class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root, key):

        # Обычная вставка узла
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Обновление высоты узла-предка
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Вычисление коэффициента баланса
        balance = self.getBalance(root)

        # Если дерево не сбалансировано, то проверяем нарушение правил и делаем повороты
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)

        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Выполнение левого поворота
        y.left = z
        z.right = T2

        # Обновление высоты узлов
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Выполнение правого поворота
        y.right = z
        z.left = T3

        # Обновление высоты узлов
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):

        if not root:
            return

        self.inOrder(root.left)
        print("{0} ".format(root.key), end="")
        self.inOrder(root.right)

    def postOrder(self, root):

        if not root:
            return

        self.postOrder(root.left)
        self.postOrder(root.right)
        print("{0} ".format(root.key), end="")

    def search(self, root, key):

        # Если дерево пустое или ключ находится в корне
        if not root or root.key == key:
            return root

        # Если ключ меньше значения корневого узла, рекурсивно ищем в левом поддереве
        if root.key > key:
            return self.search(root.left, key)

        # Если ключ больше значения корневого узла, рекурсивно ищем в правом поддереве
        return self.search(root.right, key)

    def delete(self, root, key):

        # Шаг 1: Удаление узла из бинарного дерева поиска
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:  # key == root.key

            # Узел с одним или без детей
            if not root.left:
                temp = root.right
                root = None
                return temp

            elif not root.right:
                temp = root.left
                root = None
                return temp

            # Узел с двумя детьми: Найдем наименьший элемент в правом поддереве (минимальный элемент в правом поддереве)
            # и используйте его в качестве замены удаляемого элемента
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # Если дерево имеет только один узел, то его нет необходимости балансировать
        if not root:
            return root

        # Шаг 2: Обновление высоты узла-предка
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Шаг 3: Проверка правил AVL-дерева и выполнение поворотов
        balance = self.getBalance(root)

        # Нарушение правил на левой стороне дерева
        if balance > 1:

            # LL (Left Left) случай
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)

            # LR (Left Right) случай
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        # Нарушение правил на правой стороне дерева
        elif balance < -1:

            # RR (Right Right) случай
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)

            # RL (Right Left) случай
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)


tree = AVLTree()
root = None

root = tree.insert(root, 10)
root = tree.insert(root, 20)
root = tree.insert(root, 30)
root = tree.insert(root, 40)

print("Дерево до удаления элемента 20:")
tree.inOrder(root)

root = tree.delete(root, 20)

print("\nДерево после удаления элемента 20:")
tree.inOrder(root)
