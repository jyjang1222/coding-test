import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        String data = scan.nextLine();
        String[] numArr = data.split(" ");
        System.out.println(Integer.parseInt(numArr[0]) + Integer.parseInt(numArr[1]));    
    }
}