class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def author(self) -> str:
        return self._author

    @property
    def name(self) -> str:
        return self._name


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int = None):
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages) -> None:
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float = None):
        super().__init__(name, author)
        self._duration = duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration) -> None:
        if not isinstance(duration, float):
            raise TypeError
        if duration < 0:
            raise ValueError
        self._duration = duration
