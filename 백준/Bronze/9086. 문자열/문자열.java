import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	int num = scan.nextInt();
    	scan.nextLine();
    	
    	for (int i = 0; i < num; i++) {
    		String str = scan.nextLine();
			String[] strList = str.split("");
			System.out.println(strList[0] + strList[str.length() - 1]);
		}
    	
    	scan.close();
    }
}