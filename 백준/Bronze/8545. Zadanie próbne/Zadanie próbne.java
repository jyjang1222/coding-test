import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	String[] strList = scan.nextLine().split("");
    	String res = "";
    	
    	for (int i = 0; i < strList.length; i++) {
    		int idx = (strList.length-1) - i;
    		res += strList[idx];
    	}
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}