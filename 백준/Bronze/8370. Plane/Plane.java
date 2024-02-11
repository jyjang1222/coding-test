import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

    	Scanner scan = new Scanner(System.in);
    	String[] str = scan.nextLine().split(" ");
    	int[] temp = new int[4];
    	
    	for (int i = 0; i < temp.length; i++) {
    		temp[i] = Integer.parseInt(str[i]);
    	}
    	
    	int res = temp[0] * temp[1] + temp[2] * temp[3];
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}