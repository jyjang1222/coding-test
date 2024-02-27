import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

    	Scanner scan = new Scanner(System.in);
    	
    	int x = scan.nextInt();
    	int y = scan.nextInt();
    	
    	int res = 4;
    	
    	if (x > 0 && y > 0) {
    		res = 1;
    	} else if (x < 0 && y > 0) {
    		res = 2;
    	} else if (x < 0 && y < 0) {
    		res = 3;
    	}
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}