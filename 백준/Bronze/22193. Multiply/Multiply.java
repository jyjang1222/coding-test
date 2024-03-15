import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	String temp = scan.nextLine();
    	
    	int A = scan.nextInt();
    	int B = scan.nextInt();
    	int res = A * B;
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}