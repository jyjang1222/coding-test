//import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
//import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws Exception {
    	
//    	Scanner scan = new Scanner(System.in);
    	
//    	LocalDateTime localDateTime = LocalDateTime.now();
    	ZonedDateTime zonedDateTime = ZonedDateTime.now(ZoneId.of("UTC"));
    	DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
    	String formmatedDateTime = zonedDateTime.format(formatter);
//    	System.out.println(formmatedDateTime);
    	
    	String[] date = formmatedDateTime.split("-");
    	
    	System.out.println(date[0]);
    	System.out.println(date[1]);
    	System.out.println(date[2]);
    	
//    	scan.close();
    }
}