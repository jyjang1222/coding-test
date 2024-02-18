import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	int testNum = scan.nextInt();
    	scan.nextLine();
    	
    	for (int i = 0; i < testNum; i++) {
    		String[] numList = scan.nextLine().split(" ");
    		int num1 = Integer.parseInt(numList[0]);
    		int num2 = Integer.parseInt(numList[1]);
    		int res = num1 + num2;
    		System.out.println(res);    		
    	}
    	
    	scan.close();
    }
}