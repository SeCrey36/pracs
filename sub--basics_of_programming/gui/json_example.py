import json

def add_airplane(data):
        json_str = {'name': 'pl1',
                    'e_seats': 10*[0],
                    'e_price': 10,
                    'b_seats': 20*[0],
                    'b_price': 20,
                    'f_seats': 30*[0],
                    'f_price': 30,
                    }
        with open('sub--basics_of_programming/another/gui/cfg/data.json', 'w', encoding="utf-8") as f:
            # data = load_json()
            data.append(json_str)
            json.dump(data, f)


def load_data():
    try:
        with open('sub--basics_of_programming/another/gui/cfg/data.json', 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
print(load_data())
add_airplane(load_data())