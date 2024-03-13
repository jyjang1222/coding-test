import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	String[] bottleList = scan.nextLine().split(" ");
    	int total = 0;
    	
    	for (String bottle : bottleList) {
    		total += Integer.parseInt(bottle);
    	}
    	total *= 5;
    	
    	System.out.println(total);
    	
    	scan.close();
    }
}