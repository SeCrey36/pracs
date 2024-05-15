package prac5;

public class House {
  /*
   * Класс "дом"
   */

  // Приватные поля класса
  private int number_rooms;
  private int cost;
  private double square;
  private String soundproof;
  private String apartment_renovation;
  private Boolean parking;
  private int number_bathroom;

  // Конструктор по умолчанию
  public House() {
    setNumberRooms(1);
    setCost(1);
    setSquare(1);
    setSoundproof("Undefined");
    setApartmentRenovation("Undefined");
    setParking(false);
    setNumberBathroom(0);
  }

  // Конструктор с параметрами
  public House(int rooms_field, int costField, double squareField,
      String soundField, String renovField, Boolean parkingField, int bathField) {
    // Инициализация полей класса
    setNumberRooms(rooms_field);
    setCost(costField);
    setSquare(squareField);
    setSoundproof(soundField);
    setApartmentRenovation(renovField);
    setParking(parkingField);
    setNumberBathroom(bathField);

  }

  // Геттеры и сеттеры для каждого поля класса
  public int getNumberBathroom() {
    return number_bathroom;
  }

  public void setNumberBathroom(int integerField) {
    try {
      if (integerField >= 0) {
        this.number_bathroom = integerField;
      } else {
        throw new NegativeValueException("Количество ванных комнат не может быть отрицательным.");
      }
    } catch (NegativeValueException e) {
      System.out.println("Number Format ERR");
    }
  }

  public int getNumberRooms() {
    return number_rooms;
  }

  public void setNumberRooms(int integerField) {
    try {
      if (integerField <= 0) {
        throw new NegativeValueException("Количество комнат должно быть положительным числом.");
      } else {
        this.number_rooms = integerField;
      }
    } catch (NegativeValueException e) {
      System.out.println("Number Format ERR");
    }
  }

  public int getCost() {
    return cost;
  }

  public void setCost(int integerField) {
    try {
      if (integerField >= 0) {
        this.cost = integerField;
      } else {
        throw new NegativeValueException("Стоимость должна быть неотрицательным числом.");
      }
    } catch (NegativeValueException e) {
      System.out.println("Number Format ERR");
    }
  }

  public double getSquare() {
    return square;
  }

  public void setSquare(double doubleField) {
    try {
      if (doubleField > 0) {
        this.square = doubleField;
      } else {
        throw new NegativeValueException("Площадь должна быть положительным числом.");
      }
    } catch (NegativeValueException e) {
      System.out.println("Number Format ERR");
    }
  }

  public String getSoundproof() {
    return soundproof;
  }

  public void setSoundproof(String textField1) {
    try {
      if (textField1.isEmpty()) {
        throw new InvalidInputException("Не может быть пустым полем");
      } else {
        this.soundproof = textField1;
      }
    } catch (InvalidInputException e) {
      System.out.println(e.getMessage());
    }
  }

  public String getApartmentRenovation() {
    return apartment_renovation;
  }

  public void setApartmentRenovation(String textField2) {
    try {
      if (textField2.isEmpty()) {
        throw new InvalidInputException("Не может быть пустым полем");
      } else {
        this.apartment_renovation = textField2;
      }
    } catch (InvalidInputException e) {
      System.out.println(e.getMessage());
    }
  }

  public Boolean getParking() {
    return parking;
  }

  public void setParking(Boolean parkingBoolean) {
    this.parking = parkingBoolean;
  }
}
