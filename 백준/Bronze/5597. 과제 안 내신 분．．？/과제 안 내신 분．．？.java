import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Map<String, Integer> numList = new HashMap<String, Integer>();
    	Scanner scan = new Scanner(System.in);

    	
    	for (int i = 1; i <= 30; i++) {
    		numList.put(String.valueOf(i), null);
    	}
    	
    	for (int i = 1; i <= 28; i++) {
    		int num = scan.nextInt();
    		
    		numList.put(String.valueOf(num), num);
    	}
    	
    	ArrayList<Integer> printList = new ArrayList<Integer>();
    	
    	for (String key : numList.keySet()) {
    		if (numList.get(key) == null) {
    			printList.add(Integer.parseInt(key));
    		}
    	}
    	
    	if (printList.get(0) > printList.get(1)) {
    		System.out.println(printList.get(1));
    		System.out.println(printList.get(0));
    	} else {
    		System.out.println(printList.get(0));
    		System.out.println(printList.get(1));
    	}
    	
    	scan.close();
    }
}