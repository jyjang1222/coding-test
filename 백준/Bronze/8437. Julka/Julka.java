import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	// total = natalia + klaudia
    	// klaudia = natalia + gap
    	// natalia = klaudia - gap
    	// gap = klaudia - natalia
    	// total = 2klaudia - gap
    	// total = 2natalia + gap
    	// klaudia = (total + gap) / 2
    	// natalia = (total - gap) / 2
    	
    	BigInteger total = new BigInteger(scan.nextLine());
    	BigInteger gap = new BigInteger(scan.nextLine());
    	
    	BigInteger klaudia = total.add(gap).divide(BigInteger.valueOf(2));
    	BigInteger natalia = klaudia.subtract(gap);
    			
    	System.out.println(klaudia);
    	System.out.println(natalia);
    	
    	scan.close();
    }
}