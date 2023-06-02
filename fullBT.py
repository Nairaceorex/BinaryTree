class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


def build_full_binary_tree(array):
    if not array:
        return None

    if len(array) == 1:
        return Node(array[0])

    mid = len(array) // 2
    root = Node(array[mid])
    root.left = build_full_binary_tree(array[:mid])
    root.right = build_full_binary_tree(array[mid + 1:])
    if not root.left and root.right:
        root.left = Node()
    elif root.left and not root.right:
        root.right = Node()

    return root


def print_pyramid_tree(root, level=0, direction=""):
    """
    Функция для отображения бинарного дерева в виде пирамиды в консоли.
    """
    if root is not None:
        print(" " * (level * 4) + direction, root.val)
        print_pyramid_tree(root.left, level + 1, "/")
        print_pyramid_tree(root.right, level + 1, "\\")


# Пример использования
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = build_full_binary_tree(arr)
print_pyramid_tree(tree)
