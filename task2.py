import random
from AVLTree import AVLTree


def find_min_value(node):
    """
    Знаходить найменше значення у дереві, коренем якого є заданий вузол.
    """
    current = node
    while current and current.left:
        current = current.left
    return current.key if current else None


def main():
    """Main function"""
    avl_tree = AVLTree()
    keys = random.sample(range(-100, 100), 15)

    for key in keys:
        avl_tree.insert_key(key)

    print(avl_tree)

    max_value = find_min_value(avl_tree.get_root())
    print("Найменше значення в AVL-дереві:", max_value)


if __name__ == "__main__":
    main()
