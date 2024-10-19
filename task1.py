import random

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def get_height(node):
    """
    Get the height of the node.
    """
    if not node:
        return 0
    return node.height


def get_balance(node):
    """
    Get the balance factor of the node.
    """
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def left_rotate(z):
    """
    Perform a left rotation on the subtree rooted with z.
    """
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def right_rotate(y):
    """
    Perform a right rotation on the subtree rooted with y.
    """
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def min_value_node(node):
    """
    Get the node with the smallest key value found in the tree.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current


def insert(root, key):
    """
    Insert a node with the given key into the AVL tree.
    """
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def delete_node(root, key):
    """
    Delete a node with the given key from the AVL tree.
    """
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def find_max_value(node):
    """
    Find the maximum value in the AVL tree.
    """
    current = node
    # Traverse the rightmost node to find the maximum value
    while current and current.right:
        current = current.right

    return current.key if current else None

def main():
    """ Main function """
    root = None
    # keys = [10, 20, 25, 28, 27, -1, 30]
    keys = random.sample(range(-100, 100), 15)

    for key in keys:
        root = insert(root, key)
        print("Вставлено:", key)
        print("AVL-Дерево:")
        print(root)

    for key in keys:
        root = insert(root, key)

    max_value = find_max_value(root)
    print("Найбільше значення в AVL-дереві:", max_value)


if __name__ == "__main__":
    main()