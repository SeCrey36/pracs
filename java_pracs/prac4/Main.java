package prac4;

import java.util.Scanner;

/**
 * Main class
 */
public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int[] arr = null;

    while (true) {
      System.out.println("Menu:");
      System.out.println("1. Fill the array");
      System.out.println("2. Calculate and display results");
      System.out.println("3. Exit");

      System.out.println("Enter your choice:");
      int choice = scanner.nextInt();

      switch (choice) {
        case 1:
          // Add el to array
          System.out.println("Enter the size of the array:");
          int size = scanner.nextInt();
          arr = new int[size];
          System.out.println("Enter the elements of the array:");
          for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
          }
          break;
        case 2:
          // Print result
          if (arr == null) {
            System.out.println("Array is not filled yet!");
          } else {
            PrimeCounter primeCounter = new PrimeCounter();
            int primeCount = primeCounter.fold(arr);

            NotPrimeCounter notPrimeCounter = new NotPrimeCounter();
            int notPrimeCount = notPrimeCounter.fold(arr);

            System.out.println("Number of prime numbers: " + primeCount);
            System.out.println("Number of non-prime numbers: " + notPrimeCount);
          }
          break;
        case 3:
          // Exit from program  
          System.out.println("Exiting the program...");
          scanner.close();
          System.exit(0);
        default:
          System.out.println("Invalid choice! Please enter a valid option.");
      }
    }
  }
}
