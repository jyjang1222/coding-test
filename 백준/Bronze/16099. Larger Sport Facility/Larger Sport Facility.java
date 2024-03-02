import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	int num = scan.nextInt();
    	scan.nextLine();
    	
    	long TelecomParisTech = 0; 
    	long Eurecom = 0;
    	String res = "";
    	
    	for (int i = 0; i < num; i++) {
    		String[] data = scan.nextLine().split(" ");
    		
    		res = "Tie";
    		TelecomParisTech = Long.parseLong(data[0]) * Long.parseLong(data[1]);
    		Eurecom = Long.parseLong(data[2]) * Long.parseLong(data[3]);
    		
    		if (Eurecom > TelecomParisTech) {
    			res = "Eurecom";
    		} else if (Eurecom < TelecomParisTech) {
    			res = "TelecomParisTech";
    		}
    		
    		System.out.println(res);
		}	
        	
    	scan.close();
    }
}