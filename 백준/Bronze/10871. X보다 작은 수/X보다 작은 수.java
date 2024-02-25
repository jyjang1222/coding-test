import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {

    	Scanner scan = new Scanner(System.in);
    	
    	String[] AX = scan.nextLine().split(" ");
//    	String A = AX[0];
    	int X = Integer.parseInt(AX[1]);
    	String[] strNum = scan.nextLine().split(" ");
    	
    	String res = "";
    	for (int i = 0; i < strNum.length;i++) {
    		if (X > Integer.parseInt(strNum[i])) {
    			res += strNum[i];
    			if (i < strNum.length - 1) {
    				res += " ";
    			}
    		}
    	}
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}