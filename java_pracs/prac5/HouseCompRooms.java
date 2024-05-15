package prac5;

import java.util.Comparator;

class HouseCompRooms implements Comparator<House> {
    /*
    Компаратор количества комнат
    */
    @Override
    public int compare(House house1, House house2) {
      return (int) house1.getNumberRooms() - (int) house2.getNumberRooms();
    }
}

