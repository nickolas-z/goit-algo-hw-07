import random
from AVLTree import AVLTree


def find_sum(node):
    """
    Обчислює суму всіх значень у дереві, починаючи з заданого вузла.
    """
    if node is None:
        return 0
    return node.key + find_sum(node.left) + find_sum(node.right)


def main():
    """Main function"""
    avl_tree = AVLTree()
    keys = random.sample(range(-100, 100), 15)

    for key in keys:
        avl_tree.insert_key(key)

    print(avl_tree)

    sum_tree = find_sum(avl_tree.get_root())
    print("Сума всіх значень в AVL-дереві:", sum_tree)


if __name__ == "__main__":
    main()
