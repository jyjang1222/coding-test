import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int R = scan.nextInt();
		int S = scan.nextInt();
		
		int totalCupcake = R * 8 + S * 3;
		int student = 28;
		int remainedCupcake = totalCupcake - student;
		remainedCupcake = (remainedCupcake < 0) ? 0 : remainedCupcake;
		
		System.out.println(remainedCupcake);
		
		scan.close();
	}

}