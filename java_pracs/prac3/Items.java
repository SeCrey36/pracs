package prac3;

import java.util.Objects;

public class Items {
  protected int price;
  protected String name;

  public Items() {
    // Default constructor
  }

  public Items(int price, String name) {
    this.price = price;
    this.name = name;
  }

  public int getPrice() {
    return price;
  }

  public void setPrice(int integerField) {
    if (integerField >= 0) {
      this.price = integerField;
    }
  }

  public String getName() {
    return name;
  }

  public void setName(String strField) {
    this.name = strField;
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null || getClass() != obj.getClass())
      return false;
    Items items = (Items) obj;
    return price == items.price && Objects.equals(name, items.name);
  }

  @Override
  public String toString() {
    return "Items{" +
        "price=" + price +
        " name=" + name +
        '}';
  }

  @Override
  public int hashCode() {
    return Objects.hash(price, name);
  }
}