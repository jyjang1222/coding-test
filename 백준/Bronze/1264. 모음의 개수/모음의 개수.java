import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {		
		
		Scanner scan = new Scanner(System.in);
		char[] chList = {'a', 'e', 'i', 'o', 'u'};
		
		while (true) {
			String str = scan.nextLine().toLowerCase();
			if (str.equals("#")) {
				break;
			}
			
			int count = 0;
			for (int i = 0; i < str.length(); i++) {
				char ch = str.charAt(i);
				
				for (char c : chList) {
					if (ch == c) {
						count += 1;
					}
				}
			}
			System.out.println(count);
			
		}
		scan.close();
		
	}

}