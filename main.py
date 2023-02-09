if __name__ == "__main__":
    class VideoGame:
        def __init__(self, name: str, weight: float):
            """
            Создание и подготовка к работе объекта "Видеоигра"

            :param name: Название игры
            :param weight: Объём занимаемой памяти в Гб

            Примеры:
            >>> grand_theft_auto = VideoGame('Grand Theft Auto 5', 108.53) # инициализация экземпляра класса
             """
            self._name = name # защищенный атрибут, потому что пользователь не может изменить имя игры
            self._weight = weight # защищенный атрибут, потому что пользователь не может изменить вес игры

        def __str__(self) -> str:
            return f'Видеоигра "{self._name}". Требуемый объём памяти: {self._weight} Гб.'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name = {self._name!r}, weight = {self._weight})'

        def install_game(self, free_space: float) -> float:
            """
            С помощью этой функции мы устанавливаем игру на устройство.

            :param free_space: Количество свободной памяти на устройстве в Гб

            Примеры:
            >>> limbo = VideoGame('LIMBO', 150 / 1024)
            >>> limbo.install_game(640.3)
            """
            if free_space < self._weight:
                raise ValueError('Недостаточно места на диске!')
            return free_space - self._weight

        def uninstall_game(self, free_space: float) -> float:
            """
            С помощью этой функции мы устанавливаем игру на устройство.

            :param free_space: Количество свободной памяти на устройстве в Гб

            Примеры:
            >>> limbo = VideoGame('LIMBO', 150 / 1024)
            >>> limbo.uninstall_game(640.3)
            """
            return free_space + self._weight


    class SinglePlayerGame(VideoGame):
        def __init__(self, name: str, weight: float, gameplay_hours: int):
            """
            Создание и подготовка к работе объекта "Одиночная видеоигра"

            :param name: Название игры
            :param weight: Объём занимаемой памяти в Гб
            :param gameplay_hours: Число часов геймплея

            Примеры:
            >>> the_witcher_3 = SinglePlayerGame('The Wither 3: Wild Hunt', 57.76, 100) # инициализация экземпляра класса
             """
            super().__init__(name, weight)
            self._gameplay_hours = gameplay_hours # защищенный атрибут, потому что пользователь не может изменить количество геймлейных часов игры

        def __str__(self) -> str:
            return f'Одиночная видеоигра "{self._name}". Требуемый объём памяти: {self._weight} Гб. Количество часов геймлея: {self._gameplay_hours}.'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name = {self._name!r}, weight = {self._weight}, gameplay_hours = {self._gameplay_hours})'

        @staticmethod
        def save_progress(save_cell: int) -> str:
            """
            С помощью этой функции мы сохраняем игру в выбранной ячейке сохранения.

            :param save_cell: Номер ячейки сохранения в списке.

            Примеры:
            >>> the_witcher_3 = SinglePlayerGame('The Wither 3: Wild Hunt', 57.76, 100)
            >>> the_witcher_3.save_progress(2)
            """
            return f'Игра сохранена в ячейке сохранения {save_cell}'

        @staticmethod
        def load_progress(save_cell: int) -> str:
            """
            С помощью этой функции мы загружаем игру из вывбранной ячейки сохранения.

            :param save_cell: Номер ячейки сохранения в списке.

            Примеры:
            >>> the_witcher_3 = SinglePlayerGame('The Wither 3: Wild Hunt', 57.76, 100)
            >>> the_witcher_3.load_progress(2)
            """
            return f'Загрузка сохранения в ячейке сохранения {save_cell}.'


    class OnlineGame(VideoGame):
        def __init__(self, name: str, weight: float, average_online: int):
            """
            Создание и подготовка к работе объекта "Онлайн-видеоигра"

            :param name: Название игры
            :param weight: Объём занимаемой памяти в Гб
            :param average_online: Среднее число онлайн-игроков.

            Примеры:
            >>> dota_2 = OnlineGame('Dota 2', 15, 573592) # инициализация экземпляра класса
             """
            super().__init__(name, weight)
            self._average_online = average_online # защищенный атрибут, потому что пользователь не может изменить количество онлайн-игроков

        def __str__(self) -> str:
            return f'Онлайн-игра "{self._name}". Требуемый объём памяти: {self._weight} Гб. Среднее количество онлайн-игроков: {self._average_online}.'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}(name = {self._name!r}, weight = {self._weight}, average_online = {self._average_online})'

        @staticmethod
        def find_match() -> None:
            """
            С помощью этой функции мы запускаем поиск матча внутри игры.

            Примеры:
            >>> dota_2 = OnlineGame('Dota 2', 15, 573592)
            >>> dota_2.find_match()
           """
            ...







