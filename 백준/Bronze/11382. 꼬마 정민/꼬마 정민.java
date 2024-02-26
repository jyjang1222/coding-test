import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

    	Scanner scan = new Scanner(System.in);
    	
    	String[] strNumList = scan.nextLine().split(" ");
    	long num = 0;
    	
    	for (String strNum : strNumList) {
    		num += Long.parseLong(strNum);
    	}
    	
    	System.out.println(num);
    	
    	scan.close();
    }
}