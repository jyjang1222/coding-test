import java.util.Scanner;

public class Main {
	
	public static int solution(int x) {
		int res = x * x * x;
		return res;
	}
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int X = scan.nextInt();
		
		int result = solution(X);
		
		System.out.println(result);
		
		scan.close();
	}

}