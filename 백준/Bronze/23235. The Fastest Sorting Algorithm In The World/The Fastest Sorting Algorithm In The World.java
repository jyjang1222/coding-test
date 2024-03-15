import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	int check = -1;
    	int i = 1;
    	    	
    	while (check != 0) {
    		String tc = scan.nextLine();
    		check = Character.getNumericValue(tc.charAt(0));
    		if (check != 0) {
    			System.out.printf("Case %d: Sorting... done!\n", i);    			
    		}
    		i += 1;
    	}
    	
    	scan.close();
    }
}