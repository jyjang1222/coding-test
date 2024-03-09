import java.util.Scanner;
import java.math.*;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	String[] numList = scan.nextLine().split(" ");
    	
    	double num1 = Double.parseDouble(numList[0])+1;
    	double num2 = Double.parseDouble(numList[1])+1;
    	double num3 = Double.parseDouble(numList[2])+1;
    	
    	double res = num1 * num2;
    	res /= num3;
    	res -= 1;
    	int result = (int)Math.floor(res);
    	
    	System.out.println(result);
    	
    	scan.close();
    }
}