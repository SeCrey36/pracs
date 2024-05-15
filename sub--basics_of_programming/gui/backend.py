"""Practical 6"""
import json

class Main:
    """Class main: обёрточный класс для взаимодействия"""
    def __init__(self):
        self.airplanes = []
        self.airplane = None

    def select_airplane(self, ind):
        """Func: select airplane from aiprlanes list"""
        self.airplane = self.airplanes[int(ind)]

    def list_airplanes(self):
        temp = []
        for i, pl_class in enumerate(self.airplanes):
            temp.append(str(i) +' '+ str(pl_class.name))
        return temp

    def add_airplane_object(self, info):
        """Func: add airplane to airplanes list"""
        airplane = Airplane(info[0])
        zone1 = Zone("Economy Class", "Low", info[1]*[0],
                      info[2])
        zone2 = Zone("Business Class", "Medium", info[3]*[0],
                     info[4])
        zone3 = Zone("First Class", "High", info[5]*[0],
                     info[6])
        airplane.zones = [zone1, zone2, zone3]
        self.airplanes.append(airplane)

    def del_airplane(self, ind):
        """Func: delete airplane from airplanes list"""
        self.airplanes.remove(self.airplane)
        self.airplane = None
        data = Main.load_json(self)
        data.pop(int(ind))
        with open('sub--basics_of_programming/gui/cfg/data.json',
                    'w', encoding="utf-8") as f:
            json.dump(data, f)


    def plane_info(self):
        """Func: print airplane info"""
        temp = ''
        pl_name, zones = self.airplane.plane_info()
        temp += f'Plane name: {pl_name}\n\n'
        for zone in zones:
            temp+= str(zone)+'\n'
        return temp


    def booking(self, inp_zone, seat):
        """Func: booking"""
        if self.airplane is not None:
            if inp_zone == 1:
                print(self.airplane.reserve_seat(self.airplane.zones[0],
                int(seat)))
            elif inp_zone == 2:
                print(self.airplane.reserve_seat(self.airplane.zones[1],
                int(seat)))
            elif inp_zone == 3:
                print(self.airplane.reserve_seat(self.airplane.zones[2],
                int(seat)))
            else:
                print('Incorrect')
        else:
            print('Choose airplane!')

    def del_book(self, inp_zone, seat):
        """Func: delete booking"""
        if inp_zone == 1:
            print(self.airplane.del_reserve(self.airplane.zones[0], int(seat)))
        elif inp_zone == 2:
            print(self.airplane.del_reserve(self.airplane.zones[1], int(seat)))
        elif inp_zone == 3:
            print(self.airplane.del_reserve(self.airplane.zones[2], int(seat)))



    def load_json(self):
        try:
            with open('sub--basics_of_programming/gui/cfg/data.json',
                      'r', encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return FileNotFoundError

    def add_airplane(self, data, info, syncflag):
        if syncflag == 0:
            json_str = {'name': info[0],
                        'e_seats': info[1]*[0],
                        'e_price': info[2],
                        'b_seats': info[3]*[0],
                        'b_price': info[4],
                        'f_seats': info[5]*[0],
                        'f_price': info[6],
                        }
            with open('sub--basics_of_programming/gui/cfg/data.json',
                    'w', encoding="utf-8") as f:
                data.append(json_str)
                json.dump(data, f)
        Main.add_airplane_object(self, info)

    def seats(self, zone):
        if zone == 1:
            return self.airplane.zones[0].seats
        if zone == 2:
            return self.airplane.zones[1].seats
        if zone == 3:
            return self.airplane.zones[2].seats


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
            if zone.seats[seat_number] == 0:
                zone.seats[seat_number] = 1
                return f"Seat {seat_number} in {zone.name} reserved."
            return f"No available seats in {zone.name}."
        except IndexError:
            print('IndexError')
            return 'Error'

    @staticmethod
    def del_reserve(zone, seat_number):
        """Func: delete booking"""
        try:
            if zone.seats[seat_number] == 1:
                zone.seats[seat_number] = 0
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
