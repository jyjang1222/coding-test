import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {		
		Scanner scan = new Scanner(System.in);
		String str = scan.nextLine();
		
		if (str.equals("N") || str.equals("n")) {
			System.out.println("Naver D2");
		} else {
			System.out.println("Naver Whale");
		}
	}

}