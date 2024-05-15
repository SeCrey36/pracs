package prac5;

public class InvalidInputException extends Exception {
    /*
    Класс ошибки "Некорректный ввод"
    */
    public InvalidInputException() {
        super();
      }
    
      public InvalidInputException(String message) {
        super(message);
      }
    
      public InvalidInputException(String message, Throwable cause) {
        super(message, cause);
      }
    
      public InvalidInputException(Throwable cause) {
        super(cause);
      }
}
