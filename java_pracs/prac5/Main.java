package prac5;

//Входные данные: параметры для обьекта "квартира"
//Результат работы алгоритма: вывод информации, редактирование информации

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.InputMismatchException;
import java.util.List;
import java.util.logging.*;

public class Main {
  /*
   * Main класс, точка входа в программу
   */
  @SuppressWarnings("resource")
  public static void main(String[] args) {
    Logger logger = Logger.getLogger(Main.class.getName());
    ArrayList<House> houses = new ArrayList<House>();
    System.out.println("Hello there in Practical 5! Commands:");
    System.out.println("------------------------------------");
    while (true) {
      Scanner command = new Scanner(System.in);
      System.out.println("\n1. Add an empty object");
      System.out.println("2. Add object");
      System.out.println("3. Edit field");
      System.out.println("4. Print all objects info");
      System.out.println("5. Sort");
      System.out.println("6. Filter by price");
      System.out.println("0. Exit");
      try {
        int s = command.nextInt();
        command.nextLine();
        switch (s) {
          case 0:
            // Выход из программы
            command.close();
            System.exit(-1);
          case 1:
            // Добавить пустой дом
            houses.add(new House());
            System.out.println("Empty object added!");
            break;
          case 2:
            // Добавить дом с описанием
            System.out.print("Number of rooms (int): ");
            int rooms = command.nextInt();
            System.out.print("Cost (int): ");
            int cost = command.nextInt();
            System.out.print("Square (double): ");
            double square = command.nextDouble();
            command.nextLine();

            String sound = "Undefined";
            String renov = "Undefined";
            try {
              System.out.print("Soundproof (str): ");
              sound = command.nextLine();
              System.out.print("Apartment renovation (str): ");
              renov = command.nextLine();
            } catch (Exception e) {
              logger.severe("Wrong str input!");
            }

            Boolean parking = false;
            try {
              System.out.print("Parking (true/false): ");
              parking = command.nextBoolean();
            } catch (InputMismatchException e) {
              logger.log(Level.WARNING, "Invalid input! Please enter 'true' or 'false'. Default: false");
              command.nextLine();
            }
            System.out.print("Bathrooms: ");
            int bath = command.nextInt();
            command.nextLine();
            try {
              houses.add(new House(rooms, cost, square, sound, renov, parking, bath));
              System.out.println("Оbject added!");
            } catch (IllegalArgumentException e) {
              e.printStackTrace();
              System.out.println("Оbject NOT added!");
            }
            break;
          case 3:
            // Правка информации по дому
            if (houses.size() > 0) {
              System.out.println("Select house:");
              assert !houses.isEmpty() : "Houses array is empty";
              System.out.println(shortInfo(houses));
              int choice_house = command.nextInt();
              assert (choice_house >= 0 && choice_house < houses.size()) : "Incorrect index!";
              command.nextLine();
              System.out.println("Select field:\n1. Rooms\n2. Cost\n3. Square\n4. Soundproof\n" +
                  "5. Renovation\n6. Parking\n7. Bathrooms");
              int choice_field = command.nextInt();
              command.nextLine();
              switch (choice_field) {
                case 1:
                  houses.get(choice_house).setNumberRooms(command.nextInt());
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
                  houses.get(choice_house).setApartmentRenovation(command.nextLine());
                  break;
                case 6:
                  houses.get(choice_house).setParking(command.nextBoolean());
                  break;
                case 7:
                  houses.get(choice_house).setNumberBathroom(command.nextInt());
                  command.nextLine();
                  break;
                default:
                  System.out.println("Invalid choice!");
                  break;
              }
            } else {
              System.out.println("U havent houses!");
            }
            break;
          case 4:
            // Вывод списка домов
            if (houses.size() > 0) {
              System.out.println(fullInfo(houses));
            } else {
              System.out.println("U havent houses!");
            }
            break;
          case 5:
            // Сортировка домов по выбранному критерию
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
          case 6:
            // Фильтрация по цене
            System.out.println("Print max price for filter:");
            int maxPrice = command.nextInt();
            command.nextLine();
            List<House> filteredHouses = filterByPrice(houses, maxPrice);
            filteredHouses.forEach(System.out::println);
            break;
          default:
            System.out.println("IDK this command :(");
            break;
        }
      } catch (InputMismatchException e) {
        // подавление исключения
      }
    }
  }

  public static String shortInfo(ArrayList<House> houses) {
    /*
     * Метод возвращает строку для выбора конкретного дома по индексу
     */
    return "Choose a house:\n" +
        houses.stream()
            .map(house -> {
              int rooms = house.getNumberRooms();
              int cost = house.getCost();
              return "Rooms: " + rooms + ". Cost: " + cost + ".";
            })
            .reduce("", (res, info) -> res + info + "\n");
  }

  public static String fullInfo(ArrayList<House> houses) {
    /*
     * Метод возвращает строку полной информации по всем квартирам
     * Также возвращается стоимость одного квардрата (полная/квадраты)
     */
    return houses.stream()
        .map(house -> {
          int rooms = house.getNumberRooms();
          int cost = house.getCost();
          double square = house.getSquare();
          String sound = house.getSoundproof();
          String renov = house.getApartmentRenovation();
          boolean parking = house.getParking();
          int bath = house.getNumberBathroom();
          double square_cost = cost / square;
          return "House " + houses.indexOf(house) +
              ". Rooms: " + rooms +
              ". Cost: " + cost +
              "p. Square: " + square +
              "m2. Soundproof: " + sound +
              ". Renovation: " + renov +
              ". Parking: " + parking +
              ". Bathrooms: " + bath +
              ". Square cost (calculated): " +
              String.format("%.2f", square_cost) + "p.";
        })
        .reduce("", (res, info) -> res + info + "\n");
  }

  public static List<House> filterByPrice(ArrayList<House> houses, int maxPrice) {
    // Фильтрация объектов по цене
    return houses.stream()
                 .filter(house -> house.getCost() < maxPrice)
                 .collect(Collectors.toList());
}
