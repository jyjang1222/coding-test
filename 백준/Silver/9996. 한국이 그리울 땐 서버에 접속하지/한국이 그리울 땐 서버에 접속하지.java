import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
    	Scanner scan = new Scanner(System.in);
    	
    	int num = scan.nextInt();
    	scan.nextLine();
    	
    	String[] pattern = scan.nextLine().split("\\*");
    	String startPattern = pattern[0];
    	String endPattern = pattern[1];
    	int startPatternLen = pattern[0].length();
    	int endPatternLen = pattern[1].length();
    	int patternLen = startPatternLen + endPatternLen;
    	
    	String res = "";
    	
    	for (int i = 0; i < num; i++) {
    		res = "NE";
    		String fileName = scan.nextLine();
    		int fileNameLen = fileName.length();
    		int startIdx = (fileName.length() - 1) - (endPatternLen - 1); 

    		// 파일이름 길이가 패턴길이보다 작을 경우
    		if (startPatternLen > fileNameLen || endPatternLen > fileNameLen) {
    			System.out.println(res);
    			continue;
    		}
    		
    		// 앞뒤패턴이 같을 경우 a*a a, aaa*a aaa
    		if (patternLen > fileNameLen) {
    			System.out.println(res);
    			continue;
    		}
    		
    		String slicedStartName = fileName.substring(0, startPatternLen);
    		String slicedEndName = fileName.substring(startIdx);
    		
    		if (slicedStartName.equals(startPattern) && slicedEndName.equals(endPattern)) {
    			res = "DA";
    		}
    		
    		System.out.println(res);
    	}
    	
    }
}