import doctest
from typing import Union

# TODO Написать 3 класса с документацией и аннотацией типов

class Candies:
    def __init__(self, number_of_candies: int, flavor: str):
        '''
        Создание и подготовка к работе объекта "Конфеты в банке"

        :param number_of_candies: Количество конфет в банке
        :param flavor: Вкус конфет

        Примеры:
        >>> apple_candies = Candies(15, 'Apple') # инициализация экземпляра класса
        '''
        if not isinstance(number_of_candies, int):
            raise TypeError('Число конфет должно быть целым числом!')
        if not number_of_candies > 0:
            raise ValueError('Число конфет должно быть положительным числом')
        self.number_of_candies = number_of_candies
        self.flavor = flavor


    def add_candies(self, number_of_added_candies: int):
        '''
        С помощью этой функции мы добавляем определённое количество конфет в банку.

        :param number_of_added_candies: Число конфет, которое мы добавляем.

        Примеры:
        >>> apple_candies = Candies(15, 'Apple')
        >>> apple_candies.add_candies(5)
        '''
        if not isinstance(number_of_added_candies, int):
            raise TypeError('Число конфет должно быть целым числом!')
        if not number_of_added_candies > 0:
            raise ValueError('Число конфет должно быть положительным числом')
        ...

    def take_candies(self, number_of_taken_candies: int):
        '''
        С помощью этой функции мы берём определённое количество конфет из банки.

        :param number_of_taken_candies: Число конфет, которое мы берём.
        :raise ValueError: Если мы забираем конфет больше, чем есть в банке, то вызываем ошибку.

        Примеры:
        >>> apple_candies = Candies(15, 'Apple')
        >>> apple_candies.take_candies(5)
        '''
        if not isinstance(number_of_taken_candies, int):
            raise TypeError('Число конфет должно быть целым числом!')
        if not number_of_taken_candies > 0:
            raise ValueError('Число конфет должно быть положительным числом')
        ...


class HardDrive:
    def __init__(self, memory_size: Union[int, float], used_memory: Union[int, float]):
        '''
        Создание и подготовка к работе объекта "Жёсткий диск"

        :param memory_size: Объём памяти
        :param used_memory: Объём занятой памяти

        Примеры:
        >>> C_drive = HardDrive(1024, 513) # инициализация экземпляра класса
        '''

        if not isinstance(memory_size, (int, float)):
            raise TypeError
        if memory_size <= 0:
            raise ValueError
        self.memory_size = memory_size

        if not isinstance(used_memory, (int, float)):
            raise TypeError
        if used_memory <= 0:
            raise ValueError
        if used_memory > memory_size:
            raise ValueError
        self.used_memory = used_memory


    def free_space(self):
        '''
        Функция, показывающая, сколько осталось свободного места на носителе.

        :return: Объём свободной памяти.

        Примеры:
        >>> disk = HardDrive(2048, 500)
        >>> disk.free_space()
        '''
        ...


    def delete_files(self, deleted_memory: Union[int, float]):
        '''
        Освобождает заданное количество памяти на носителе.

        :param deleted_memory: Объём освобождаемой памяти.
        :raise ValueError: Если объём освбождаемой памяти превышает объём занятой памяти, то возвращается ошибка.
        :raise ValueError: Если объём освбождаемой памяти превышает максимальный объём памяти, то возвращается ошибка.

        Примеры:
        >>> disk = HardDrive(2048, 1900)
        >>> disk.delete_files(500)
        '''
        ...


class DebitCard:
    def __init__(self, balance: Union[int, float], income: Union[int, float], expences: Union[int, float]):
        '''
        Создание и подготовка к работе объекта "Дебетовая карта"

        :param balance: Текущий баланс.
        :param income: Доходы за опр. период времени.
        :param expences: Расходы за тот же промежуток.

        Примеры:
        >>> sber_card = DebitCard(5000.14, 11665, 9962) # инициализация экземпляра класса
        '''

        if not isinstance(balance, (int, float)):
            raise TypeError
        if balance <= 0:
            raise ValueError
        self.balance = balance

        if not isinstance(income, (int, float)):
            raise TypeError
        if income <= 0:
            raise ValueError
        self.income = income

        if not isinstance(expences, (int, float)):
            raise TypeError
        if expences <= 0:
            raise ValueError
        self.expences = expences

    def earning(self, amount: Union[int, float]):
        '''
        Поступление средств на карту.

        :param amount: Денежная сумма, поступившая на карту.

        Пример:
        >>> card = DebitCard(5900, 13443, 9445)
        >>> card.earning(5000)
        '''
        if not isinstance(amount, (int, float)):
            raise TypeError
        if amount <= 0:
            raise ValueError


    def spending(self, amount: Union[int, float]):
        '''
        Расход средств с карты.

        :param amount: Потраченная сумма.
        :raise ValueError: Если потраченная сумма превышает текущий баланс на карте, то возвращается ошибка.

        Пример:
        >>> card = DebitCard(5900, 13443, 9445)
        >>> card.spending(3999)
        '''
        if not isinstance(amount, (int, float)):
            raise TypeError
        if amount <= 0:
            raise ValueError
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()

