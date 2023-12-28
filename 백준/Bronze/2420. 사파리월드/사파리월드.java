import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        String data = scan.nextLine();
        String[] numArr = data.split(" ");
        long res = Long.parseLong(numArr[0]) - Long.parseLong(numArr[1]);
        res = (res < 0) ? res *= -1 : res; 
        System.out.println(res);
    }
}