import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	String[] matrixSize = scan.nextLine().split(" ");
    	int matrixRow = Integer.parseInt(matrixSize[0]);
    	int matrixCol = Integer.parseInt(matrixSize[1]);
    	
    	int[][] matrix = new int[matrixRow][matrixCol];
    	
    	for (int i = 0; i < matrixRow * 2; i++) {
    		String[] value = scan.nextLine().split(" ");
    		for (int j = 0; j < matrixCol; j++) {
    			int rowIdx = i % matrixRow;
    	    	matrix[rowIdx][j] = matrix[rowIdx][j] + Integer.parseInt(value[j]);
			}
    	}
    	
    	for (int[] row : matrix) {
//    		System.out.println(Arrays.toString(row));
    		String print = "";
    		for (int data : row) {
//    			System.out.print(data + " ");
    			print += data + " ";
    		}
    		System.out.println(print.trim());
    	}
    	
    } // main() end
}