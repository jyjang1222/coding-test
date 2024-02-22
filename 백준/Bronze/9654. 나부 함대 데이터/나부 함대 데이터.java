public class Main {
    public static void main(String[] args) throws Exception {

    	String[][] list = {
    		{"SHIP NAME", "CLASS", "DEPLOYMENT", "IN SERVICE"},
    		{"N2 Bomber", "Heavy Fighter", "Limited", "21"},
    		{"J-Type 327", "Light Combat", "Unlimited", "1"},
    		{"NX Cruiser", "Medium Fighter", "Limited", "18"},
    		{"N1 Starfighter", "Medium Fighter", "Unlimited", "25"},
    		{"Royal Cruiser", "Light Combat", "Limited", "4"}
    	};
    	
    	String data = "";
    	
    	for (int i = 0; i < list.length; i++) {
    		data += String.format("%-15s%-15s%-11s%-10s", list[i][0], list[i][1], list[i][2], list[i][3]);
    		data += "\n";
		}
    	
    	System.out.println(data);
    }
}