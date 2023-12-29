import java.util.Scanner;
//import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {

// 1회차 배열로 풀기
//    	Scanner scan = new Scanner(System.in);
//    	String[] matrixSize = scan.nextLine().split(" ");
//    	int matrixRow = Integer.parseInt(matrixSize[0]);
//    	int matrixCol = Integer.parseInt(matrixSize[1]);
//    	
//    	int[][] matrix = new int[matrixRow][matrixCol];
//    	
//    	for (int i = 0; i < matrixRow * 2; i++) {
//    		String[] value = scan.nextLine().split(" ");
//    		for (int j = 0; j < matrixCol; j++) {
//    			int rowIdx = i % matrixRow;
//    	    	matrix[rowIdx][j] = matrix[rowIdx][j] + Integer.parseInt(value[j]);
//			}
//    	}
//    	
//    	for (int[] row : matrix) {
////    		System.out.println(Arrays.toString(row));
//    		String print = "";
//    		for (int data : row) {
////    			System.out.print(data + " ");
//    			print += data + " ";
//    		}
//    		System.out.println(print.trim());
//    	}
    	
// 2회차 연결리스트로 풀기
    	Scanner scan = new Scanner(System.in);
    	String[] matrixSize = scan.nextLine().split(" ");
    	
    	int matrixRow = Integer.parseInt(matrixSize[0]);
    	int matrixCol = Integer.parseInt(matrixSize[1]);
    	
    	ArrayList<String[]> matrix1 = new ArrayList<String[]>();
    	ArrayList<String[]> matrix2 = new ArrayList<String[]>();
    	
    	for (int i = 0; i < matrixRow * 2; i++) {
    		String[] dataArr = scan.nextLine().split(" ");
			if (i < matrixRow) {
				matrix1.add(dataArr);
			} else {
				matrix2.add(dataArr);
			}
    	} 
    	
    	for (int i = 0; i < matrixRow; i++) {
    		String res = "";
    		for (int j = 0; j < matrixCol; j++) {
				int data1 = Integer.parseInt(matrix1.get(i)[j]);
				int data2 = Integer.parseInt(matrix2.get(i)[j]);
				res += data1 + data2 + " ";
			}
    		System.out.println(res.trim());
    	}
    	
    } // main() end
}
