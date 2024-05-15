//Входные данные: параметры для обьекта "квартира"
//Результат работы алгоритма: вывод информации, редактирование информации

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.InputMismatchException;

class House {
  private int number_rooms;
  private int cost;
  private double square;
  private String soundproof;
  private String apartment_renovation;
  private Boolean parking;
  private int number_bathroom;

  public House() {
    // Конструктор по умолчанию
  }

  public House(int rooms_field, int costField, double squareField,
      String soundField, String renovField, Boolean parkingField, int bathField) {
    this.number_rooms = rooms_field;
    this.cost = costField;
    this.square = squareField;
    this.soundproof = soundField;
    this.apartment_renovation = renovField;
    this.parking = parkingField;
    this.number_bathroom = bathField;
  }

  // Методы доступа (геттеры и сеттеры) для каждого поля
  public int getNumber_bathroom() {
    return number_bathroom;
  }

  public void setNumber_bathroom(int integerField) {
    if (integerField >= 0) {
      this.number_bathroom = integerField;
    }
  }

  public int getNumber_rooms() {
    return number_rooms;
  }

  public void setNumber_rooms(int integerField) {
    if (integerField > 0) {
      this.number_rooms = integerField;
    }
  }

  public int getCost() {
    return cost;
  }

  public void setCost(int integerField) {
    if (integerField >= 0) {
      this.cost = integerField;
    }
  }

  public double getSquare() {
    return square;
  }

  public void setSquare(double doubleField) {
    if (doubleField > 0) {
      this.square = doubleField;
    }
  }

  public String getSoundproof() {
    return soundproof;
  }

  public void setSoundproof(String textField1) {
    if (textField1 instanceof String) {
      this.soundproof = textField1;
    } else {
      System.out.println("Type error!");
    }
  }

  public String getApartment_renovation() {
    return apartment_renovation;
  }

  public void setApartment_renovation(String textField2) {
    if (textField2 instanceof String) {
      this.apartment_renovation = textField2;
    } else {
      System.out.println("Type error!");
    }
    this.apartment_renovation = textField2;
  }

  public Boolean getParking() {
    return parking;
  }

  public void setParking(Boolean parkingBoolean) {
    this.parking = parkingBoolean;
  }
}

// Классы для сортировки массива
class HouseCompCost implements Comparator<House> {
  @Override
  public int compare(House house1, House house2) {
    return house1.getCost() - house2.getCost();
  }
}

class HouseCompSquare implements Comparator<House> {
  @Override
  public int compare(House house1, House house2) {
    return (int) house1.getSquare() - (int) house2.getSquare();
  }
}

class HouseCompRooms implements Comparator<House> {
  @Override
  public int compare(House house1, House house2) {
    return (int) house1.getNumber_rooms() - (int) house2.getNumber_rooms();
  }
}

public class Prac2 {
  public static void main(String[] args) {
    ArrayList<House> houses = new ArrayList<House>();
    System.out.println("Hello there in Practical 2! Commands:");
    System.out.println("------------------------------------");
    while (true) {
      Scanner command = new Scanner(System.in);
      System.out.println("\n1. Add an empty object");
      System.out.println("2. Add object");
      System.out.println("3. Edit field");
      System.out.println("4. Print all objects info");
      System.out.println("5. Sort");
      System.out.println("6. Exit");
      try {
        int s = command.nextInt();
        command.nextLine(); // остаток строки \n
        switch (s) {
          case 6:
            command.close();
            System.exit(-1);
          case 1:
            houses.add(new House());
            System.out.println("Empty object added!");
            break;
          case 2:
            System.out.print("Number of rooms (int): ");
            int rooms = command.nextInt();
            System.out.print("Cost (int): ");
            int cost = command.nextInt();
            System.out.print("Square (double): ");
            double square = command.nextDouble();
            command.nextLine();
            System.out.print("Soundproof (str): ");
            String sound = command.nextLine();
            System.out.print("Apartment renovation (str): ");
            String renov = command.nextLine();
            System.out.print("Parking (true/false): ");
            Boolean parking = command.nextBoolean();
            System.out.print("Bathrooms: ");
            int bath = command.nextInt();
            command.nextLine();
            houses.add(new House(rooms, cost, square, sound, renov, parking, bath));
            System.out.println("Оbject added!");
            break;
          case 3:
            if (houses.size() > 0) {
              System.out.println("Select house:");
              System.out.println(shortInfo(houses));
              int choice_house = command.nextInt();
              command.nextLine();
              if (choice_house >= 0 && choice_house < houses.size()) {
                System.out.println("Select field:\n1. Rooms\n2. Cost\n3. Square\n4. Soundproof\n" +
                    "5. Renovation\n6. Parking\n7. Bathrooms");
                int choice_field = command.nextInt();
                command.nextLine();
                switch (choice_field) {
                  case 1:
                    houses.get(choice_house).setNumber_rooms(command.nextInt());
                    command.nextLine();
                    break;
                  case 2:
                    houses.get(choice_house).setCost(command.nextInt());
                    command.nextLine();
                    break;
                  case 3:
                    houses.get(choice_house).setSquare(command.nextDouble());
                    command.nextLine();
                    break;
                  case 4:
                    houses.get(choice_house).setSoundproof(command.nextLine());
                    break;
                  case 5:
                    houses.get(choice_house).setApartment_renovation(command.nextLine());
                    break;
                  case 6:
                    houses.get(choice_house).setParking(command.nextBoolean());
                    break;
                  case 7:
                    houses.get(choice_house).setNumber_bathroom(command.nextInt());
                    command.nextLine();
                    break;
                  default:
                    System.out.println("Invalid choice!");
                    break;
                }
              } else {
                System.out.println("Incorrect house!");
              }
            } else {
              System.out.println("U havent houses!");
            }
            break;
          case 4:
            if (houses.size() > 0) {
              System.out.println(fullInfo(houses));
            } else {
              System.out.println("U havent houses!");
            }
            break;
          case 5:
            if (houses.size() > 0) {
              System.out.println("Sort by:\n1. Cost\n2. Square\n3. Rooms");
              int choise = command.nextInt();
              command.nextLine();
              System.out.println(choise);
              switch (choise) {
                case 1:
                  Collections.sort(houses, new HouseCompCost());
                  break;
                case 2:
                  Collections.sort(houses, new HouseCompSquare());
                  break;
                case 3:
                  Collections.sort(houses, new HouseCompRooms());
                  break;
                default:
                  System.out.println("Invalid choice!");
                  break;
              }
            } else {
              System.out.println("U havent houses!");
            }
            break;
          default:
            System.out.println("IDK this command :(");
            break;
        }
      } catch (InputMismatchException e) {
        System.out.println("Invalid command or input!");
      }
    }
  }

  public static String shortInfo(ArrayList<House> houses) {
    /*
     * Метод возвращает строку для выбора конкретного дома по индексу
     */
    String res = "Choose a house:\n";
    for (int i = 0; i < houses.size(); i++) {
      int rooms = houses.get(i).getNumber_rooms();
      int cost = houses.get(i).getCost();

      res = res + i + ". Rooms: " + rooms + ". Cost: " + cost + ". \n";
    }
    return res;
  }

  public static String fullInfo(ArrayList<House> houses) {
    /*
     * Метод возвращает строку полной информации по всем квартирам
     * Также возвращается стоимость одного квардрата (полная/квадраты)
     */
    String res = "";
    for (int i = 0; i < houses.size(); i++) {
      int rooms = houses.get(i).getNumber_rooms();
      int cost = houses.get(i).getCost();
      double square = houses.get(i).getSquare();
      String sound = houses.get(i).getSoundproof();
      String renov = houses.get(i).getApartment_renovation();
      Boolean parking = houses.get(i).getParking();
      int bath = houses.get(i).getNumber_bathroom();
      double square_cost = cost / square;
      res = res + "House " + i +
          ". Rooms: " + rooms +
          ". Cost: " + cost +
          "p. Square: " + square +
          "m2. Soundproof: " + sound +
          ". Renovation: " + renov +
          ". Parking: " + parking +
          ". Bathrooms: " + bath +
          ". Square cost (calculated): " +
          String.format("%.2f", square_cost) + "p.\n";
    }
    return res;
  }
}
