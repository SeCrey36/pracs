package prac3;

import java.util.Objects;

public class Products extends Items {
  private String type;
  private int count;

  public Products() {
    // Default constructor
  }

  public Products(int price, String name, String type, int count) {
    super(price, name);
    this.type = type;
    this.count = count;
  }

  public String getType() {
    return type;
  }

  public void setType(String type) {
    this.type = type;
  }

  public int getCount() {
    return count;
  }

  public void setCount(int count) {
    if (count >= 0) {
      this.count = count;
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
    Products products = (Products) obj;
    return count == products.count && Objects.equals(type, products.type);
  }

  @Override
  public String toString() {
    return "Products{" +
        "price=" + price +
        ", name=" + name +
        ", type=" + type +
        ", count=" + count +
        '}';
  }

  @Override
  public int hashCode() {
    return Objects.hash(super.hashCode(), type, count);
  }
}
