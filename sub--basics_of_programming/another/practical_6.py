"""Practical 6"""
import sys


class Main:
    """Class main: обёрточный класс для взаимодействия"""
    def __init__(self):
        self.airplanes = []
        self.airplane = None

    def select_airplane(self):
        """Func: select airplane from aiprlanes list"""
        try:
            for i, pl_class in enumerate(self.airplanes):
                print(i, pl_class.name)
            self.airplane = self.airplanes[int(input('Input number of plane: '))]
        except IndexError:
            print('Index Error / 0 airplanes')
        except ValueError:
            print('Input must be int')

    def add_airplane(self):
        """Func: add airplane to airplanes list"""
        airplane = Airplane(input('Input airplane name: '))
        zone1 = Zone("Economy Class", "Low", int(input('Eco seats: '))*[0],
                     int(input('Eco price: ')))
        zone2 = Zone("Business Class", "Medium", int(input('Business seats: '))*[0],
                     int(input('Business price: ')))
        zone3 = Zone("First Class", "High", int(input('Elite seats: '))*[0],
                     int(input('Elite price: ')))
        airplane.zones = [zone1, zone2, zone3]
        self.airplanes.append(airplane)

    def del_airplane(self):
        """Func: delete airplane from airplanes list"""
        self.airplanes.remove(self.airplane)
        self.airplane = None

    def plane_info(self):
        """Func: print airplane info"""
        if self.airplane is not None:
            pl_name, zones = self.airplane.plane_info()
            print(f'Plane name: {pl_name}')
            for zone in zones:
                print(zone)
        else:
            print('Choose airplane!')

    def booking(self):
        """Func: booking"""
        if self.airplane is not None:
            inp_zone = int(input(f'What zone u want? '
                                    f'(1 - eco ({self.airplane.zones[0].price}), '
                                    f'2 - busi ({self.airplane.zones[1].price}), '
                                    f'3 - elite ({self.airplane.zones[2].price})): '))
            if inp_zone == 1:
                print(str(self.airplane.zones[0]))
                print(self.airplane.reserve_seat(self.airplane.zones[0],
                int(input('Number of seat: '))))
            elif inp_zone == 2:
                print(str(self.airplane.zones[1]))
                print(self.airplane.reserve_seat(self.airplane.zones[1],
                int(input('Number of seat: '))))
            elif inp_zone == 3:
                print(str(self.airplane.zones[2]))
                print(self.airplane.reserve_seat(self.airplane.zones[2],
                int(input('Number of seat: '))))
            else:
                print('Incorrect')
        else:
            print('Choose airplane!')



    def del_book(self):
        """Func: delete booking"""
        if self.airplane is not None:
            inp_zone = int(input('What zone u want del? (1 - eco, 2 - busi, 3 - elite): '))
            if inp_zone == 1:
                print(self.airplane.del_reserve(self.airplane.zones[0], int(input('What seat?: '))))
            elif inp_zone == 2:
                print(self.airplane.del_reserve(self.airplane.zones[1], int(input('What seat?: '))))
            elif inp_zone == 3:
                print(self.airplane.del_reserve(self.airplane.zones[2], int(input('What seat?: '))))
            else:
                print('Incorrect')
        else:
            print('Choose airplane!')


class Airplane:
    """Class airplane: сущность самолета"""
    def __init__(self, name):
        self.name = name
        self.zones = []

    def plane_info(self):
        """Func: print airplane info"""
        temp = []
        for zone in self.zones:
            temp.append(f"- Zone: {zone.name}, Tariff: {zone.tariff}, Price: {zone.price},"
                        f" Available Seats: {zone.seats.count(0)}")
        return self.name, temp

    @staticmethod
    def reserve_seat(zone, seat_number):
        """Func: booking"""
        try:
            if zone.seats[seat_number-1] == 0:
                zone.seats[seat_number-1] = 1
                return f"Seat {seat_number} in {zone.name} reserved."
            return f"No available seats in {zone.name}."
        except IndexError:
            print('IndexError')
            return 'Error'

    @staticmethod
    def del_reserve(zone, seat_number):
        """Func: delete booking"""
        try:
            if zone.seats[seat_number-1] == 1:
                zone.seats[seat_number-1] = 0
                return f"Reservation for seat {seat_number} in {zone.name} canceled."
            return f"No reservation found for seat {seat_number} in {zone.name}."
        except IndexError:
            print('IndexError')
            return 'Error'


class Zone:
    """Class zone: сущность зоны (привязана к самолету)"""
    def __init__(self, name, tariff, seats, price):
        self.name = name
        self.tariff = tariff
        self.price = price
        self.seats = seats
        

    def __str__(self):
        res = ''
        for i, el in enumerate(self.seats):
            if el:
                res += f'Место № {i+1}, цена - {self.price}, занято \n'
            else:
                res += f'Место № {i+1}, цена - {self.price}, свободно \n'
        return res

class Booking:
    """Class booking: сущность записи на рейс"""
    def __init__(self):
        self.reserved_seats = []


def main():
    """Menu: мейн функция, работает с классом main"""
    print('Hello! Its my 6rd practical. '
          'In this program u can reserve seats in airplane')
    main_thread = Main()

    actions = {
        1: main_thread.add_airplane,
        2: main_thread.plane_info,
        3: main_thread.booking,
        4: main_thread.del_book,
        5: main_thread.select_airplane,
        6: main_thread.del_airplane,
        7: sys.exit
        }

    while True:
        try:
            com = int(input('''
Commands:
    1 - add airplane
    2 - print airplane info
    3 - reserve seat
    4 - del reserve
    5 - select airplane
    6 - delete airplane
    7 - quit
        '''))
            if com in [1, 2, 3, 4, 5, 6, 7]:
                actions[com]()
            else:
                print('Incorrect com / '
                    'Not selected airplanes / '
                    '0 airplanes')
        except ValueError:
            print('ValueError')

if __name__ == '__main__':
    main()
