"""
Иерархия работников. Работа с классами
"""


class Employee:
    """
    Работник
    """

    def __init__(self, name):
        """
        :param name:
        :param salary:
        """
        self.name = name
        self.title = 'Наёмный работник'

    def get_info(self):
        """
        :return:
        """
        return ['ФИО ' + str(self.name),
                'Должность ' + str(self.title)]


class SalariedEmployee(Employee):
    """
    Работник
    """

    def __init__(self, name, salary):
        """
        :param name:
        :param salary:
        """
        Employee.__init__(self, name)
        self.title = 'Наёмный работник'
        self.salary = salary

    def get_info(self):
        """
        :return:
        """
        return ['ФИО ' + str(self.name),
                'Должность ' + str(self.title),
                'Вознаграждение ' + str(int(self.salary))]


class HourlyEmployee(Employee):
    """
    Почасовой работник
    """

    def __init__(self, name, hourly_rate, hours):
        """
        :param name:
        :param hourly_rate:
        :param hours:
        """
        Employee.__init__(self, name)
        self.hourly_rate = hourly_rate
        self.hours = hours
        self.title = 'Почасовой работник'

    def calculate_salary(self):
        """
        :return:
        """
        return int(self.hourly_rate) * int(self.hours)

    def get_info(self):
        """
        :return:
        """
        return ['ФИО ' + str(self.name),
                'Должность ' + str(self.title),
                'Почасовой оклад ' + str(self.hourly_rate),
                'Зарплата ' + str(self.calculate_salary())]


class Manager(Employee):
    """
    Менеджер
    """

    def __init__(self, name, salary, bonus):
        """
        :param name:
        :param salary:
        :param bonus:
        """
        Employee.__init__(self, name)
        self.salary = salary
        self.bonus = bonus
        self.title = 'Менеджер'

    def calculate_salary(self):
        """
        :return:
        """
        return int(self.salary) + int(self.bonus)

    def get_info(self):
        """
        :return:
        """
        return ['ФИО ' + str(self.name),
                'Должность ' + str(self.title),
                'Зарплата ' + str(self.calculate_salary()),
                'Бонус к окладу' + str(self.bonus)]


class Executive(Employee):
    """
    Руководитель
    """

    def __init__(self, name, salary, bonus, stock_options):
        """
        :param name:
        :param salary:
        :param bonus:
        :param stock_options:
        """
        Employee.__init__(self, name)
        self.salary = salary
        self.bonus = bonus
        self.stock_options = stock_options
        self.title = 'Директор'

    def calculate_salary(self):
        """
        :return:
        """
        return int(self.salary) + int(self.bonus) + int(self.stock_options)

    def get_info(self):
        """
        :return:
        """
        return ['ФИО ' + str(self.name),
                'Должность ' + str(self.title),
                'Зарплата ' + str(self.calculate_salary()),
                'Бонус к окладу' + str(self.bonus),
                'Директоральные дивиденты' + str(self.stock_options)]


class Company:
    """
    Компания
    """

    def __init__(self):
        """
        список работников
        """
        self.employees = []

    def show_employees(self):
        """
        :return:
        """
        arr = [str(self.employees[i].name) + ' '
               + str(self.employees[i].title) for i in
               range(len(self.employees))]
        return arr

    def info(self, employee_index):
        """
        :param employee_index:
        :return:
        """
        return self.employees[employee_index].get_info()

    def hire(self, employee):
        """
        :param employee:
        :return:
        """
        self.employees.append(employee)

    def fire(self, employee_index):
        """
        :param employee_index:
        :return:
        """
        self.employees.pop(employee_index)
