import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	String[] NM = scan.nextLine().split(" ");
    	
    	int res = 0;
    	
    	if(NM[0].equals(NM[1])) {
    		res = 1;
    	}
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}