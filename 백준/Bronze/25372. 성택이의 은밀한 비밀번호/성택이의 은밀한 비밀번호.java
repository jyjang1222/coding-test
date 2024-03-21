import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {		
		Scanner scan = new Scanner(System.in);
		int num = scan.nextInt();
		scan.nextLine();
		
		for (int i = 0; i < num; i++) {
			String res = "no";
			String pw = scan.nextLine();
			
			if (6 <= pw.length() && pw.length() <= 9) {
				res = "yes";
			}
			
			System.out.println(res);
		}

	}

}