import java.util.Scanner;

public class Main {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);

		while (true) {
			String memberType = "Junior";
			
			String[] member = scan.nextLine().split(" ");
			
			String memberName = member[0];
			int memberAge = Integer.parseInt(member[1]);
			int memberWeight = Integer.parseInt(member[2]);
			
			if (memberName.equals("#")) {
				break;
			}
			if (memberAge > 17 || memberWeight >= 80) {
				memberType = "Senior";
			}
			
			System.out.println(memberName + " " + memberType);
		}
		
		scan.close();
	}

}