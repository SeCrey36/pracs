package prac3;

import java.util.Objects;

public class MilkProducts extends Products {
    private int date;
    private String brand;

    public MilkProducts() {
        // Default constructor
    }

    public MilkProducts(int price, String name, String type, int count, int date, String brand) {
        super(price, name, type, count);
        this.date = date;
        this.brand = brand;
    }

    public int getDate() {
        return date;
    }

    public void setDate(int date) {
        if (date > 0) {
            this.date = date;
        }
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;
        if (!super.equals(obj))
            return false;
        MilkProducts products = (MilkProducts) obj;
        return date == products.date && Objects.equals(brand, products.brand);
    }

    @Override
    public String toString() {
        return "MilkProducts{" +
                "price=" + getPrice() +
                ", name='" + getName() + '\'' +
                ", type='" + getType() + '\'' +
                ", count=" + getCount() +
                ", date=" + date +
                ", brand='" + brand + '\'' +
                '}';
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), date, brand);
    }
}
