package prac5;

import java.util.Comparator;

public class HouseCompCost implements Comparator<House> {
    /*
    Компаратор цен
    */
    @Override
    public int compare(House house1, House house2) {
      return house1.getCost() - house2.getCost();
    }
}
  