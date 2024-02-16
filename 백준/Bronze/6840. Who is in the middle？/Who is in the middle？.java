import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	int size = 3;
    	int[] weightList = new int[size];
    	
    	Scanner scan = new Scanner(System.in);
    	
    	for (int i = 0; i < size; i++) {
    		weightList[i] = scan.nextInt();
    	}

    	for (int i = 0; i < weightList.length - 1; i++) {
			for (int j = 0; j < weightList.length - (1 + i); j++) {
				if (weightList[j] > weightList[j + 1]) {
					int temp = weightList[j + 1];
					weightList[j + 1] = weightList[j];
					weightList[j] = temp;
				}
			}
		}
    	
    	System.out.println(weightList[1]);
    }
}