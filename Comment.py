class Comment:
    def __init__(self, text, author) -> None:
        """
        Ініціалізує коментар із заданим текстом та автором.
        """
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply) -> None:
        """
        Додає відповідь до коментаря.
        """
        self.replies.append(reply)

    def remove_reply(self) -> None:
        """
        Встановлює коментар як видалений, змінюючи текст на стандартне повідомлення.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0) -> None:
        """
        Рекурсивно виводить коментар і всі його відповіді.
        """
        indent = "    " * level
        if not self.is_deleted:
            print(f"{indent}{self.author}: {self.text}")
        else:
            print(f"{indent}{self.text}")
        for reply in self.replies:
            reply.display(level + 1)


if __name__ == "__main__":
    # Створення коментарів
    comment1 = Comment("Це перший коментар", "Автор1")
    comment2 = Comment("Це відповідь на перший коментар", "Автор2")
    comment3 = Comment("Це ще одна відповідь на перший коментар", "Автор3")
    comment4 = Comment("Це відповідь на другу відповідь", "Автор4")

    # Додавання відповідей
    comment1.add_reply(comment2)
    comment1.add_reply(comment3)
    comment2.add_reply(comment4)

    # Відображення коментарів
    comment1.display()

    # Видалення коментаря
    comment2.remove_reply()

    # Відображення коментарів після видалення
    comment1.display()
