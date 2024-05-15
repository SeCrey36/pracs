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
                'Вознаграждение ' + str(self.salary)]


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

    def change_title(self, employee_index, new_title,
                     new_salary, hourly_rate, hours, bonus, stock_options):
        """
        grand костыль
        """
        old_employee = self.employees[employee_index]
        if new_title == 'Hourly':
            if not isinstance(old_employee, HourlyEmployee):
                employee = HourlyEmployee(old_employee.name,
                                          hourly_rate, hours)
                self.employees[employee_index] = employee
        elif new_title == 'Manager':
            if not isinstance(old_employee, Manager):
                employee = Manager(old_employee.name, new_salary, bonus)
                self.employees[employee_index] = employee
        elif new_title == 'Executive':
            if not isinstance(old_employee, Executive):
                employee = Executive(old_employee.name,
                                     new_salary, bonus, stock_options)
                self.employees[employee_index] = employee
        elif new_title == 'Freelancer':
            if not isinstance(old_employee, Manager):
                employee = SalariedEmployee(old_employee.name, new_salary)
                self.employees[employee_index] = employee


def main():
    """
    Основная программа
    """
    company = Company()
    while True:
        try:
            option_choice = input("1 - Информация о сотрудниках;\n"
                                  "2 - Узнать информацию о сотруднике;\n"
                                  "3 - Добавить сотрудника;\n"
                                  "4 - Удалить сотрудника;\n"
                                  "5 - Повысить сотрудника;\n"
                                  "0 - Закончить программу;\n")
            match option_choice:
                case "1":
                    employee_list = company.show_employees()
                    _ = [print(str(i + 1) + ' ' + employee_list[i])
                         for i in range(len(employee_list))]
                case "2":
                    employee_list = company.show_employees()
                    _ = [print(str(i + 1) + ' ' + employee_list[i])
                         for i in range(len(employee_list))]
                    try:
                        employee_index = int(input('Выберите номер'
                                                   ' работника о котором'
                                                   ' хотите узнать'
                                                   ' информацию: '))
                        info_arr = company.info(employee_index - 1)
                        _ = [print(info_arr[i]) for i in range(len(info_arr))]
                    except IndexError:
                        print('Index Error')
                case "3":
                    try:
                        title_choice = input("Кого вы хотите добавить?\n"
                                             "Наёмный работник(1)\n"
                                             "Почасовой работник(2)\n"
                                             "Менеждер(3)\n"
                                             "Руководитель(4): \n")

                        match title_choice:
                            case '1':
                                name = input('Введите ФИО: ')
                                salary = int(input('Введите его зарплату: '))
                                employee = SalariedEmployee(name, salary)
                                company.hire(employee)
                            case '2':
                                name = input('Введите ФИО: ')
                                hourly_rate = int(input('Введите его'
                                                        ' почасовой оклад: '))
                                hours = int(input('Введите количество'
                                                  ' часов работы: '))
                                employee = HourlyEmployee(name, hourly_rate,
                                                          hours)
                                company.hire(employee)
                            case '3':
                                name = input('Введите ФИО: ')
                                salary = int(input('Введите его зарплату: '))
                                bonus = int(input('Введите бонус к окладу: '))
                                employee = Manager(name, salary, bonus)
                                company.hire(employee)
                            case '4':
                                name = input('Введите ФИО: ')
                                salary = int(input('Введите его зарплату: '))
                                bonus = int(input('Введите бонус к окладу: '))
                                stock_options = int(input('Введите'
                                                          ' директоральные'
                                                          ' дивиденты: '))
                                employee = Executive(name, salary, bonus,
                                                     stock_options)
                                company.hire(employee)
                    except ValueError:
                        print('Value Error')
                    except IndexError:
                        print('Index Error')
                case "4":
                    employee_list = company.show_employees()
                    _ = [print(str(i + 1) + employee_list[i]) for
                         i in range(len(employee_list))]
                    if len(company.employees) > 0:

                        try:
                            employee_index = int(input('Выберите'
                                                       ' номер работника'
                                                       ' которого хотите'
                                                       ' уволить: '))
                            company.fire(employee_index - 1)
                        except IndexError:
                            print('Index Error')
                    else:
                        print("Ещё нет сотрудников")
                case "5":
                    employee_list = company.show_employees()
                    _ = [print(str(i + 1) + employee_list[i])
                         for i in range(len(employee_list))]
                    if len(company.employees) > 0:
                        try:
                            employee_index = int(input('Выберите номер'
                                                       ' работника о'
                                                       ' которого хотите'
                                                       ' повысить'))
                            new_title = input('Выберете новую должность:\n'
                                              "Наёмный работник(1)\n"
                                              "Почасовой работник(2)\n"
                                              "Менеждер(3)\n"
                                              "Руководитель(4): \n")
                            match new_title:
                                case '1':
                                    salary = int(input('Введите его зарплату: '))
                                    company.change_title(employee_index - 1,
                                                         'Employee', salary,
                                                         0, 0, 0, 0)
                                case '2':
                                    hourly_rate = int(input('Введите'
                                                            ' его почасовой'
                                                            ' оклад: '))
                                    hours = int(input('Введите'
                                                      ' количество часов'
                                                      ' работы: '))
                                    company.change_title(employee_index - 1,
                                                         'Hourly', 0,
                                                         hourly_rate,
                                                         hours, 0, 0)
                                case '3':
                                    salary = int(input('Введите его'
                                                       ' зарплату: '))
                                    bonus = int(input('Введите бонус'
                                                      ' к окладу: '))
                                    company.change_title(employee_index - 1,
                                                         'Manager',
                                                         salary, 0, 0,
                                                         bonus, 0)
                                case '4':
                                    salary = int(input('Введите'
                                                       ' его зарплату: '))
                                    bonus = int(input('Введите бонус'
                                                      ' к окладу: '))
                                    stock_options = input('Введите '
                                                          'директоральные'
                                                          ' дивиденты: ')
                                    company.change_title(employee_index - 1,
                                                         'Executive',
                                                         salary, 0, 0, bonus,
                                                         stock_options)
                        except IndexError:
                            print('Index Error')
                        except ValueError:
                            print('Value Error')
                    else:
                        print('Ещё нет сотрудников')
                case "0":
                    break
        except (IndexError, ValueError):
            print("error")


if __name__ == '__main__':
    main()
