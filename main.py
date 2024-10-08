# 1. Создать класс Computer с приватными атрибутами cpu и memory
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # 2. Добавить сеттеры и геттеры к существующим атрибутам
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    # 3. Метод make_computations для арифметических вычислений
    def make_computations(self):
        return self.cpu * self.memory

    # 9. Переопределить магический метод str
    def __str__(self):
        return f"Computer(cpu={self.cpu}, memory={self.memory})"

    # 10. Перезаписать магические методы сравнения по атрибуту memory
    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


# 4. Создать класс Phone с приватным полем sim_cards_list
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # 5. Добавить сеттеры и геттеры
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    # 6. Метод call с параметром sim_card_number и call_to_number
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Неверный номер сим-карты")

    # 9. Переопределить магический метод str
    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"


# 7. Создать класс SmartPhone, наследуемый от Computer и Phone
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # 8. Метод use_gps
    def use_gps(self, location):
        print(f"Построение маршрута до {location}...")

    # 9. Переопределить магический метод str
    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"


# 11. Создать объекты компьютера, телефона и смартфонов
computer = Computer(cpu=3.2, memory=16)
phone = Phone(sim_cards_list=["Beeline", "Megacom"])
smartphone1 = SmartPhone(cpu=2.8, memory=8, sim_cards_list=["O!", "Tele2"])
smartphone2 = SmartPhone(cpu=3.5, memory=12, sim_cards_list=["Beeline", "Megacom"])

# 12. Распечатать информацию о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# 13. Опробовать методы каждого объекта
# Компьютер
print(f"Вычисление (cpu * memory) для компьютера: {computer.make_computations()}")

# Телефон
phone.call(1, "+996 777 99 88 11")

# Смартфон 1
smartphone1.use_gps("Бишкек")
smartphone1.call(2, "+996 555 77 66 55")

# Смартфон 2
print(f"Сравнение смартфонов по памяти: {smartphone2 > smartphone1}")