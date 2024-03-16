import java.util.Scanner;

public class Main {
	
	public static int divide(int x, int num) {
		int subtractResult = x - num;
		
		if (subtractResult > 0) {
			return divide(subtractResult, num);		
		} else if (subtractResult == 0) {
			return subtractResult;
		}
		return x;
	}
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int X = scan.nextInt();
		final int NUM = 21;
		
		int result = divide(X, NUM);
		
		System.out.println(result);
		
		scan.close();
	}

}