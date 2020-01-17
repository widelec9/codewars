package kyu5;

public class Scramblies {

	public static boolean scramble(String str1, String str2) {
		for (char c : str2.chars().distinct().toString().toCharArray()) {
			if (str1.chars().filter(ch -> ch == c).count() < str2.chars().filter(ch -> ch == c).count()) {
				return false;
			}
		}
		return true;
	}
}