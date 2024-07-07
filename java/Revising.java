import java.util.Scanner;

public class Revising {
  
  public static void main(String[] args) {
   System.out.println("Print something"); 
   Scanner scan = new Scanner(System.in);
   String name = scan.nextLine();
   System.out.println(hi(name));
  }


  public  static String hi(String name) {
    return "hi" + ' ' + name;
  }
}
