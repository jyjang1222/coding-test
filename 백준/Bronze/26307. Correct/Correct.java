import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {		
		Scanner scan = new Scanner(System.in);
		String[] time = scan.nextLine().split(" ");
		int startTime = 540;
		int endTime = Integer.parseInt(time[0]) * 60 + Integer.parseInt(time[1]);
		
		int usageTime = endTime - startTime;
		
		System.out.println(usageTime);
	
	}

}