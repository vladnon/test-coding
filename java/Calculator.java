import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
      System.out.println("ok");
      Scanner scan = new Scanner(System.in);

      System.out.println("write first num");
      int num1 = scan.nextInt();

      System.out.println("write second num");
      int num2 = scan.nextInt();

      System.out.println("write sign");
      char sign = scan.next().charAt(0);

      System.out.println(calculate(num1, num2, sign));
   }

   public static int calculate (int num1, int num2, char sign) {
        return switch (sign) {
            case '+' -> num1 + num2;
            case '-' -> num1 - num2;
            case '/' -> num1 / num2;
            case '*' -> num1 * num2;
            default -> -1;
        };
   }
}
