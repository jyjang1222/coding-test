import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {		
		
		Scanner scan = new Scanner(System.in);
		String[] numList = scan.nextLine().split(" ");
		
		for (int i = 0; i < numList.length - 1; i++) {
			for (int j = 0; j < numList.length - 1 - i; j++) {
	            if (Integer.parseInt(numList[j]) > Integer.parseInt(numList[j + 1])) {
	                String temp = numList[j + 1];
	                numList[j + 1] = numList[j];
	                numList[j] = temp;
	            }
			}
		}
		
		System.out.println(String.join(" ", numList));
		
		scan.close();
	}

}