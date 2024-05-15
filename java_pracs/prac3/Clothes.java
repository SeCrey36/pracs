package prac3;

import java.util.Objects;

public class Clothes extends Items {
  private String material;
  private int size;

  public Clothes() {
    // Default constructor
  }

  public Clothes(int price, String name, String material, int size) {
    super(price, name);
    this.material = material;
    this.size = size;
  }

  public String getMaterial() {
    return material;
  }

  public void setMaterial(String material) {
    this.material = material;
  }

  public int getSize() {
    return size;
  }

  public void setSize(int size) {
    if (size >= 0) {
      this.size = size;
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
    Clothes clothes = (Clothes) obj;
    return size == clothes.size && Objects.equals(material, clothes.material);
  }

  @Override
  public String toString() {
    return "Clothes{" +
        "price=" + price +
        ", name=" + name +
        ", material=" + material +
        ", size=" + size +
        '}';
  }

  @Override
  public int hashCode() {
    return Objects.hash(super.hashCode(), material, size);
  }
}
