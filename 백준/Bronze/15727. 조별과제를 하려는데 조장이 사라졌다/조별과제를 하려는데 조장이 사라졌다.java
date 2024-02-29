import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	int distance = scan.nextInt();
    	
    	int res = distance / 5;
    	
    	if (distance % 5 != 0) {
    		res += 1;
    	}
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}