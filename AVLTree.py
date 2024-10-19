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


class AVLTree:
    def __init__(self):
        self.__root = None

    def get_root(self):
        """ Повертає корінь дерева. """
        return self.__root

    def get_height(self, node):
        """
        Повертає висоту заданого вузла.
        Якщо вузол відсутній, повертає 0.
        """
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """
        Обчислює баланс-фактор для заданого вузла.
        Баланс-фактор показує різницю між висотами лівого та правого піддерева.
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        """
        Виконує лівий поворот для заданого вузла.
        """
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        """
        Виконує правий поворот для заданого вузла.
        """
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def find_min_value(self, node):
        """
        Знаходить найменше значення у дереві, коренем якого є заданий вузол.
        """
        current = node
        while current and current.left:
            current = current.left
        return current.key if current else None

    def find_max_value(self, node):
        """
        Знаходить найбільше значення у дереві, коренем якого є заданий вузол.
        """
        current = node
        while current and current.right:
            current = current.right
        return current.key if current else None

    def insert(self, root, key):
        """
        Вставляє новий вузол з ключем у дерево.
        Повертає новий корінь дерева після вставки.
        """
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete_node(self, root, key):
        """
        Видаляє вузол з ключем із дерева.
        Повертає новий корінь дерева після видалення.
        """
        if not root:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.find_min_value(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def insert_key(self, key):
        """
        Вставляє новий ключ у дерево.
        """
        self.__root = self.insert(self.__root, key)

    def delete_key(self, key):
        """
        Видаляє ключ із дерева.
        """
        self.__root = self.delete_node(self.__root, key)

    def find_max(self):
        """
        Знаходить найбільше значення в дереві.
        """
        return self.find_max_value(self.__root)
    def find_min(self):
        """
        Знаходить найменше значення в дереві.
        """
        return self.find_min_value(self.__root)

    def __str__(self):
        """
        Повертає рядкове представлення AVL-дерева для візуалізації.
        """
        return str(self.__root) if self.__root else "Порожнє дерево"

if __name__ == "__main__":
    tree = AVLTree()

    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys:
        tree.insert_key(key)

    print("Дерево після вставки ключів:")
    print(tree)

    key_to_delete = 10
    tree.delete_key(key_to_delete)
    print(f"\nДерево після видалення ключа {key_to_delete}:")
    print(tree, end="\n\n")

    print("Найбільше значення у дереві:", tree.find_max())
    print("Найменше значення у дереві:", tree.find_min())
