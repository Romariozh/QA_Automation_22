# Завдання №1
# Розробити клас Людина.
# Людина має:
# Ім'я
# Прізвище
# Вік (атрибут але ж змінний)
# Стать
# Люди можуть:
# Їсти
# Спати
# Говорити
# Ходити
# Стояти
# Лежати
# Також ми хочемо контролювати популяцію людства. Змінювати популяцію можемо в __init__.
# Треба сказати, що доступ до статичних полів класу з __init__ не можу іти через НазваКласу.статичий_атрибут,
# позаяк ми не може бачити імені класу. Але натомість ми можемо сказати self.__class__.static_attribute.
import datetime


class Human:
    population = 0

    def __init__(self,
                 firstname: str,
                 lastname: str,
                 sex: str,
                 birth_date=datetime.date.today()):
        self.firstname = firstname
        self.lastname = lastname
        self.__birth_date = birth_date
        self.sex = sex
        self.__class__.add_population()

    @classmethod
    def add_population(cls):
        cls.population += 1

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def age(self):
        return (datetime.date.today() - self.birth_date).days // 365

    @birth_date.setter
    def birth_date(self, new_date):
        self.__birth_date = new_date

    def eat(self, food):
        print(f'I has eaten {food}, It\'s very tasty!')

    def sleep(self, place_sleep):
        print(f'I\'m going to sleep on the {place_sleep}')

    def speak(self, words):
        print(f'I think so {words}')

    def move(self, destination):
        print(f'I am going to {destination}')

    def stop(self, place_stop):
        print(f'I stopped at the {place_stop}')

    def lie(self, place_lie):
        print(f'{self.firstname} lay down on еру {place_lie}')

    def __str__(self):
        return f'[{self.firstname} {self.lastname}] birth date: {self.birth_date}'

    def __repr__(self):
        return f'Human object {self} has next param: {self.firstname} {self.lastname}'

    def __del__(self):
        print(f'Object -> {self} deleted!')


if __name__ == "__main__":
    zhan = Human('Roman', 'Ivanoov', 'male', birth_date=datetime.date(1984, 3, 26))
    print(zhan)
    print(zhan.firstname, 'is', zhan.age)
    zhan.birth_date = datetime.date(1987, 9, 20)
    print(zhan)
    print(zhan.firstname, 'is', zhan.age)
    print('Human population: ', Human.population)
