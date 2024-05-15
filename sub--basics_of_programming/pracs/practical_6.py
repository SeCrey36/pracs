import sys


class Airplane:
    def __init__(self, name, economy, business, first_class):
        self.plane_name = name
        self.economy_seats = economy
        self.business_seats = business
        self.first_class_seats = first_class
        self.lock_economy_seats = 0
        self.lock_business_seats = 0
        self.lock_first_class_seats = 0


class Zone:
    def __init__(self, name, tariff):
        self.name = name
        self.tariff = tariff


class Booking:
    def __init__(self):
        self.reserved_seats = []

    def reserve_seat(self, seat):
        self.reserved_seats.append(seat)


class Tariff:
    def __init__(self, zone, price):
        self.zone = zone
        self.price = price


def add_airplane():
    try:
        name = input('Input plane name: ')
        economy_price = int(input('Input economy price: '))
        e_seats = int(input('Input number of eco places: '))
        b_seats = int(input('Input number of business places: '))
        f_seats = int(input('Input number of 1st_class places: '))
        if e_seats >= 0 and b_seats >= 0 and f_seats >= 0 and\
                economy_price >= 0:
            return Airplane(name, e_seats, b_seats, f_seats), \
                   Zone("Economy Class", Tariff("economy", economy_price)),\
                   Zone("Business Class", Tariff("business", economy_price * 1.5)),\
                   Zone("First Class", Tariff("first_class", economy_price * 3))
        print('Incorrect value')
        return None
    except ValueError:
        print('Value Error!')


def plane_info(airplanes, plane_name):
    for airplane in airplanes:
        if airplane.plane_name == plane_name:
            temp = vars(airplane)
            info_str = f"Plane name: {temp['plane_name']}\n" \
                       f"Economy seats: {temp['economy_seats'] - temp['lock_economy_seats']}\n" \
                       f"Business seats: {temp['business_seats'] - temp['lock_business_seats']}\n" \
                       f"1st class seats: {temp['first_class_seats'] - temp['lock_first_class_seats']}\n"

            return info_str


def info_all(airplanes):
    for i, temp in enumerate(airplanes):
        info = plane_info(airplanes, temp.plane_name)
        print(f'ID plane: {i}\n' + info)


def booking(airplanes, eco_zone, busi_zone, first_zone):
    book = Booking()
    info_all(airplanes)
    id = int(input('To reserve a seat, please input the ID of the required airplane: '))
    zone = int(input(f"1. Price of eco zone: {eco_zone.tariff.price}\n"
                     f"2. Price of business zone: {busi_zone.tariff.price}\n"
                     f"3. Price of 1st class: {first_zone.tariff.price}\n"
                     f"Please enter your choice (1, 2, 3)"))

    free_eco = airplanes[id].economy_seats - airplanes[id].lock_economy_seats
    free_busi = airplanes[id].business_seats - airplanes[id].lock_business_seats
    free_first = airplanes[id].first_class_seats - airplanes[id].lock_first_class_seats

    if zone == 1 and free_eco > 0:
        book.reserve_seat({"zone": eco_zone, "seat_number": free_eco})
        airplanes[id].lock_economy_seats += 1
    elif zone == 2 and free_busi > 0:
        book.reserve_seat({"zone": busi_zone, "seat_number": free_busi})
        airplanes[id].lock_business_seats += 1
    elif zone == 3 and free_first > 0:
        book.reserve_seat({"zone": first_zone, "seat_number": free_first})
        airplanes[id].lock_first_class_seats += 1
    else:
        print('We dont have seats in this zone / '
              'Zone not find')


def main():
    """Menu

    Select action, print strings in console"""
    print('Hello! Its my 6rd practical. '
          'In this program u can reserve seats in airplane')
    airplanes = []
    while True:
        com = input('''
Commands:
    1 - add airplane
    2 - print airplane info
    3 - reserve seat
    4 - quit
        ''')
        if com == '4':
            sys.exit()
        elif com == '1':
            try:
                new_plane, eco_zone, busi_zone, first_zone = add_airplane()
                if new_plane is not None:
                    airplanes.append(new_plane)
            except TypeError:
                pass
        elif com == '2' and len(airplanes) > 0:
            info_all(airplanes)
        elif com == '3' and len(airplanes) > 0:
            booking(airplanes, eco_zone, busi_zone, first_zone)
        else:
            print('Incorrect com / '
                  '0 planes')


if __name__ == '__main__':
    main()
