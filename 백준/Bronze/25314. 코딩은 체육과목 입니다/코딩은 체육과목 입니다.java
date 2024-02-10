import java.util.Scanner;
//import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {

    	Scanner scan = new Scanner(System.in);
    	int num = scan.nextInt();
    	int quotient = num / 4;
    	String res = "";
    	
    	for (int i = 0; i < quotient; i++) {
    		res += "long ";
    	}
    	res += "int";
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}