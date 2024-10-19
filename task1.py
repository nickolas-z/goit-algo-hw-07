import random
from AVLTree import AVLTree


def find_max_value(node):
    """
    Знаходить найбільше значення у дереві, коренем якого є заданий вузол.
    """
    current = node
    while current and current.right:
        current = current.right
    return current.key if current else None

def main():
    """ Main function """
    avl_tree = AVLTree()
    root = None
    keys = random.sample(range(-100, 100), 15)

    for key in keys:
        root = avl_tree.insert_key(key)

    print(avl_tree)

    max_value = find_max_value(avl_tree.get_root())
    print("Найбільше значення в AVL-дереві:", max_value)


if __name__ == "__main__":
    main()
