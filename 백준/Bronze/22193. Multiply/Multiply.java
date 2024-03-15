import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	String temp = scan.nextLine();
    	
    	long A = scan.nextLong();
    	long B = scan.nextLong();
    	long res = A * B;
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}