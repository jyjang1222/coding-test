import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	double reward = scan.nextInt();
    	double reward20 = reward * ((double)20 / 100);
    	double TAX = 22.0;

    	double res = reward - reward * (TAX / 100);
    	double res2 = reward - reward20 * (TAX / 100);
    	
    	System.out.println((int)res);
    	System.out.println((int)res2);
    	
    	scan.close();
    }
}