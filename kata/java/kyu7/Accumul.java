package kyu7;

public class Accumul {
	public static String accum(String s) {
		String retString = "";
		String chString;
		int count = 1;
		
		for (int i = 0; i < s.length(); ++i) {
			chString = Character.toString(s.charAt(i));
			retString += chString.toUpperCase();
			retString += new String(new char[count-1]).replace("\0", chString.toLowerCase());
			if (i < s.length() - 1) {
				retString += Character.toString('-');
			}
			++count;
		}
		return retString;
	}
}