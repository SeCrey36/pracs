package prac3;

import java.util.Objects;

public class Toys extends Items {
  private int age;
  private String description;

  public Toys() {
    // Default constructor
  }

  public Toys(int price, String name, int age, String description) {
    super(price, name);
    this.age = age;
    this.description = description;
  }

  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    if (age >= 0) {
      this.age = age;
    }
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null || getClass() != obj.getClass())
      return false;
    if (!super.equals(obj))
      return false;
    Toys products = (Toys) obj;
    return age == products.age && Objects.equals(description, products.description);
  }

  @Override
  public String toString() {
    return "Products{" +
        "price=" + price +
        ", name=" + name +
        ", age=" + age +
        ", description=" + description +
        '}';
  }

  @Override
  public int hashCode() {
    return Objects.hash(super.hashCode(), age, description);
  }

}
