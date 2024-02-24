import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

    	Scanner scan = new Scanner(System.in);
    	
    	int numTotal = scan.nextInt();
    	scan.nextLine();
       	String[] numList = scan.nextLine().split(" ");
       	int numSearch = scan.nextInt();
    	
       	int total = 0;
    	for (String num : numList) {
    		if (Integer.parseInt(num) == numSearch) {
    			total += 1;
    		}
		}
    	
    	System.out.println(total);
    	
    	scan.close();
    }
}