package prac5;

public class NegativeValueException extends Exception {
    /*
    Класс ошибки "Значение меньше 0"
    */
    public NegativeValueException() {
        super();
      }
    
      public NegativeValueException(String message) {
        super(message);
      }
    
      public NegativeValueException(String message, Throwable cause) {
        super(message, cause);
      }
    
      public NegativeValueException(Throwable cause) {
        super(cause);
      }
}
