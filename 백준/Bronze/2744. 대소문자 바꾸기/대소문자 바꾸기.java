import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	String str1 = scan.nextLine();
    	String[] str = str1.split("");
    	String res = "";
    	
    	for (String ch : str) {
    		int asciiNum = (int)ch.charAt(0);
    		
    		if(65 <= asciiNum && asciiNum <= 96) { // 대문자라면
    			asciiNum += 32;
    		} else { // 소문자라면
    			asciiNum -= 32;
    		}
    		
    		res += String.valueOf((char)asciiNum);
    	}
    	
    	System.out.println(res);
    }
}