import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	String[] scoreList = scan.nextLine().split(" ");
    	
    	int UR = Integer.parseInt(scoreList[0]) * 56;
    	int TR = Integer.parseInt(scoreList[1]) * 24;
    	int UO = Integer.parseInt(scoreList[2]) * 14;
    	int TO = Integer.parseInt(scoreList[3]) * 6;
    	
    	int res = UR + TR + UO + TO;
    	System.out.println(res);
    	
    	scan.close();
    }
}