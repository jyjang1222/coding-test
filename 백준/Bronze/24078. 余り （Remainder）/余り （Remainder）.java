import java.util.Scanner;

public class Main {
	
	public static int Divide(int x, int num) {
		int subtractResult = x - num;
		
		if (subtractResult > 0) {
			return Divide(subtractResult, num);		
		} else if (subtractResult == 0) {
			return subtractResult;
		}
		return x;
	}
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int X = scan.nextInt();
		final int NUM = 21;
		
		int res = Main.Divide(X, NUM);
		
		System.out.println(res);
		
		scan.close();
	}

}
