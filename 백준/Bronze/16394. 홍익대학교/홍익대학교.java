import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	final int HONG = 1946;
    	int N = scan.nextInt();
    	int res = N - HONG;
    	System.out.println(res);

    }
}