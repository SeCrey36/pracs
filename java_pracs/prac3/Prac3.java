package prac3;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Prac3 {
    static ArrayList<Items> items = new ArrayList<>();

    public static void main(String[] args) {
        System.out.println("Hello there in Practical 3! Commands:");
        System.out.println("------------------------------------");
        while (true) {
            Scanner command = new Scanner(System.in);
            System.out.println("\n1. Add empty object");
            System.out.println("2. Add object");
            System.out.println("3. Delete object");
            System.out.println("4. Print object array");
            System.out.println("5. Test objects equals");
            System.out.println("6. Exit");
            try {
                int s = command.nextInt();
                command.nextLine();
                switch (s) {
                    case 1:
                        addEmptyObject();
                        break;
                    case 2:
                        addObject();
                        break;
                    case 3:
                        deleteObject();
                        break;
                    case 4:
                        printObjectArray();
                        break;
                    case 5:
                        testObjectsEquality();
                        break;
                    case 6:
                        command.close();
                        System.exit(0);
                    default:
                        System.out.println("Unknown command");
                        break;
                }
            } catch (InputMismatchException e) {
                System.out.println("Invalid input format!");
            }
        }
    }

    static void addEmptyObject() {
        // Ask user for object type and add empty object to the list
        System.out.println("Enter object type (1 - Products, 2 - MilkProducts, 3 - Toys, 4 - Clothes):");
        Scanner scanner = new Scanner(System.in);
        int type = scanner.nextInt();
        scanner.nextLine();
        switch (type) {
            case 1:
                items.add(new Products());
                break;
            case 2:
                items.add(new MilkProducts());
                break;
            case 3:
                items.add(new Toys());
                break;
            case 4:
                items.add(new Clothes());
                break;
            default:
                System.out.println("Invalid object type!");
                break;
        }
    }

    static void addObject() {
        // Add object with details provided by the user
        System.out.println("Enter object details:");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Price: ");
        int price = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Name: ");
        String name = scanner.nextLine();
        System.out.println("Enter object type: 1 - Products, 2 - MilkProducts, 3 - Toys, 4 - Clothes");
        int objectType = scanner.nextInt();
        scanner.nextLine();
        switch (objectType) {
            case 1:
                System.out.print("Type: ");
                String type = scanner.nextLine();
                System.out.print("Count: ");
                int count = scanner.nextInt();
                items.add(new Products(price, name, type, count));
                break;
            case 2:
                System.out.print("Type: ");
                String milkType = scanner.nextLine();
                System.out.print("Count: ");
                int milkCount = scanner.nextInt();
                System.out.print("Date: ");
                int date = scanner.nextInt();
                System.out.print("Brand: ");
                scanner.nextLine();
                String milkBrand = scanner.nextLine();
                items.add(new MilkProducts(price, name, milkType, milkCount, date, milkBrand));
                break;
            case 3:
                System.out.print("Age: ");
                int age = scanner.nextInt();
                scanner.nextLine();
                System.out.print("Description: ");
                String description = scanner.nextLine();
                items.add(new Toys(price, name, age, description));
                break;
            case 4:
                System.out.print("Material: ");
                String material = scanner.nextLine();
                System.out.print("Size: ");
                int size = scanner.nextInt();
                items.add(new Clothes(price, name, material, size));
                break;
            default:
                System.out.println("Invalid object type!");
                break;
        }
    }

    static void deleteObject() {
        // Delete object from the list based on user input
        Scanner scanner = new Scanner(System.in);
        if (items.isEmpty()) {
            System.out.println("No objects to delete.");
        } else {
            System.out.println("Enter index of object to delete:");
            int index = scanner.nextInt();
            if (index >= 0 && index < items.size()) {
                items.remove(index);
                System.out.println("Object removed successfully.");
            } else {
                System.out.println("Invalid index!");
            }
        }
    }

    static void printObjectArray() {
        // Print all objects in the list
        System.out.println("Printing object array:");
        for (Items item : items) {
            System.out.println(item);
        }
    }

    static void testObjectsEquality() {
        // Test equality between two objects in the list based on user input
        Scanner scanner = new Scanner(System.in);
        if (items.size() < 2) {
            System.out.println("At least two to check equality!");
        } else {
            System.out.println("Enter indices of objects to test equality:");
            int index1 = scanner.nextInt();
            int index2 = scanner.nextInt();
            if (index1 >= 0 && index1 < items.size() && index2 >= 0 && index2 < items.size()) {
                Items obj1 = items.get(index1);
                Items obj2 = items.get(index2);
                System.out.println("Objects are equal: " + obj1.equals(obj2));
            } else {
                System.out.println("Invalid indices!");
            }
        }
    }
}
