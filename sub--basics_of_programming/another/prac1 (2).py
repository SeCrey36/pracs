import json
import sys


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def search_by_name(routes, name):
    return [route for route in routes if route['name'] == name]


def filter_by_duration(routes, max_duration):
    return [route for route in routes if route['duration'] <= max_duration]


def routes_without_equipment(routes):
    return [route for route in routes if not route['special_equipment']]


def add_route(routes, new_route):
    routes.append(new_route)


def delete_route(routes, name):
    routes = [route for route in routes if route['name'] != name]
    return routes


def main():
    """Меню"""
    file_name = "tourist_routes.json"
    routes = load_data(file_name)
    while True:
        com = input('''
Команды: 
    1 - Выход
    2 - Выполнить поиск по имени
    3 - Фильтровать по продолжительности пути
    4 - Маршруты без спец снаряжения
    5 - Добавить запись
    6 - Удалить запись 
        ''')
        if com == '1':
            sys.exit()
        elif com == '2':
            search_name = input('Что ищем?: ')
            print(search_by_name(routes, search_name))
        elif com == '3':
            try:
                max_duration = int(input('Максимальная длина маршрута для поиска:'))
                print(filter_by_duration(routes, max_duration))
            except ValueError:
                print('Должно быть числом')
        elif com == '4':
            rts_wthout_equip = routes_without_equipment(routes)
            print(rts_wthout_equip)
        elif com == '5':
            n_route = {
                "name": input('Имя маршрута: '),
                "departure": input('От: '),
                "destination": input('До: '),
                "duration": int(input('Длительность: ')),
                "special_equipment": (input('Доп снаряжение через пробел: ').split())
            }
            add_route(routes, n_route)
            save_data(file_name, routes)
        elif com == '6':
            search_name = input('Что ищем?: ')
            routes = delete_route(routes, search_name)
            save_data(file_name, routes)
        else:
            print('Ввод некорректен')


if __name__ == '__main__':
    main()
