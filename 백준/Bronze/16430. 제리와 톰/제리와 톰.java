import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	String PQ[] = scan.nextLine().split(" ");
    	int remainder = Integer.parseInt(PQ[1]) - Integer.parseInt(PQ[0]);
    	PQ[0] = String.valueOf(remainder);
    	String res = String.join(" ", PQ);
    	
    	System.out.println(res);

    }
}