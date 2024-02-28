import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
//    	
//    	Scanner scan = new Scanner(System.in);
//    	
//    	String strList = scan.nextLine();
//    	char[] chList = strList.toCharArray();
//    	String upperStr = "";
//    	
//    	for (char ch : chList) {
//    		int gap = (int)'a' - (int)'A';
//    		int asciiNum = (int)ch;
//    		
//    		char upperCh = (char)(asciiNum - gap);
//    		upperStr += String.valueOf(upperCh);
//    	}
//    	
//    	System.out.println(upperStr);
//    	
//    	scan.close();
    	
    	Scanner scan = new Scanner(System.in);
    	
    	String strList = scan.nextLine();
    	String upperStr = strList.toUpperCase();
    	    	
    	System.out.println(upperStr);
    	
    	scan.close();
    }
}