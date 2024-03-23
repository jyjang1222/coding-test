import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {		
		
		Scanner scan = new Scanner(System.in);
		String[] ts = scan.nextLine().split(" ");
		
		int t = Integer.parseInt(ts[0]);
		int s = Integer.parseInt(ts[1]);
		int res = 280;
		
		if (12 <= t && t <= 16) {
			if (s == 0) {
				res = 320;
			}
		}
		
		System.out.println(res);
		
		scan.close();
	}

}