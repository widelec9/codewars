package kyu7;

public class Vowels {
	public static int getCount(String str) {
		String vowels = "aeiou";
		int vowelsCount = 0;
		
		for (int i = 0; i < str.length(); ++i) {
			if (vowels.indexOf(str.charAt(i)) >= 0) {
				vowelsCount++;
			}
		}
		
		return vowelsCount;
	}
}
