package prac5;

import java.util.Comparator;

public class HouseCompSquare implements Comparator<House> {
    /*
    Компаратор площади дома
    */
    @Override
    public int compare(House house1, House house2) {
      return house1.getCost() - house2.getCost();
    }
}

