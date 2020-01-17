package kyu7;

public class Isogram {
    public static boolean  isIsogram(String str) {
    	for (char letter : str.toCharArray()) {
    		if (str.chars().filter(ch -> Character.toLowerCase(ch) == letter).count() > 1) {
    			return false;
    		}
    	}
    	return true;
    } 
}