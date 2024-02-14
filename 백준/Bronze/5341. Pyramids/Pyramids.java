import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	while (true) {    		
    		int size = scan.nextInt();
    		int block = 0;
    		
    		if (size == 0) {
    			break;
    		}
    		
    		for (int i = 1; i <= size; i++) {
    			block += i;
    		}
    		
    		System.out.println(block);
    	}
    	
    	scan.close();
    }
}