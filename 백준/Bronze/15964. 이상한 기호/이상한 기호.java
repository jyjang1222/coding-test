import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	String[] AB = scan.nextLine().split(" ");
    	int A = Integer.parseInt(AB[0]);
    	int B = Integer.parseInt(AB[1]);
    	
    	int res = (A+B) * (A-B);
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}