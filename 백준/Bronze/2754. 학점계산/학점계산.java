import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	
    	Scanner scan = new Scanner(System.in);
    	
    	String grade = scan.nextLine();
    	String[] gradeList = {
    			"A+", "A0", "A-",
    			"B+", "B0", "B-",
    			"C+", "C0", "C-",
    			"D+", "D0", "D-"};
    	
    	int score = 43;
    	
    	if (grade.equals("F")) {
    		score = 0;
    	} else {
        	for (int i = 0; i < gradeList.length; i++) {
        		if (gradeList[i].equals(grade)) {
        			score -= i * 3;
        			break;
        		}
        		if (i % 3 == 2) {
        			score -= 1;
        		}
        	}
    	}

    	double res = (double)score / 10;

    	System.out.println(res);
    	
    	scan.close();
    }
}