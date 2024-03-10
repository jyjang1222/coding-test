import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	scan.nextLine();
    	char[] word = scan.nextLine().toCharArray();
    	char[] vowelList = {'a','i','u','e','o'};
    	int res = 0;
    	
    	for (char vowel : vowelList) {
    		for (char ch : word) {
    			if (ch == vowel) {
    				res += 1;
    			}
    		}
    	}
    	
    	System.out.println(res);
    	
    	scan.close();
    }
}