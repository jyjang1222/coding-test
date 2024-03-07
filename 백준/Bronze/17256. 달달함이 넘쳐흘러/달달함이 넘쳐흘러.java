import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);

    	String[] aList = scan.nextLine().split(" ");
    	String[] cList = scan.nextLine().split(" ");
    	
		int ax = Integer.parseInt(aList[0]);
		int ay = Integer.parseInt(aList[1]);
		int az = Integer.parseInt(aList[2]);
		
		int cx = Integer.parseInt(cList[0]);
		int cy = Integer.parseInt(cList[1]);
		int cz = Integer.parseInt(cList[2]);
    	
//		a cake b = (a.z + b.x, a.y × b.y, a.x + b.z)
//		a = b -> a.x = b.x, a.y = b.y, a.z = b.z
//		a cake b = c
		
//		a.z + b.x = c.x
//		a.y x b.y = c.y
//		a.x + b.z = c.z
//		b.x = c.x - a.z
//		b.y = c.y / a.y
//		b.z = c.z - a.x
		
		int bx = cx - az;
		int by = cy / ay;
		int bz = cz - ax;
		
		System.out.printf("%s %s %s", bx, by, bz);
    	
    	scan.close();
    }
}