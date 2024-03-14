import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	int N = scan.nextInt();
    	String word = "SciComLove";
    	
    	for (int i = 0; i < N; i++) {
			System.out.println(word);
		}
    	
    	scan.close();
    }
}