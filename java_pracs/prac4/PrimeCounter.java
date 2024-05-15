package prac4;

/**
 * Prime counter class
 */
class PrimeCounter implements MyInterface {
  @Override
  public int fold(int[] arr) {
    return countNumbers(arr, num -> isPrime(num));
  }

  // Counter
  private int countNumbers(int[] arr, NumberPredicate predicate) {
    int count = 0;
    for (int num : arr) {
      if (predicate.test(num)) {
        count++;
      }
    }
    return count;
  }

  // Prime checker
  private boolean isPrime(int num) {
    if (num <= 1) {
      return false;
    }
    for (int i = 2; i <= Math.sqrt(num); i++) {
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }
}