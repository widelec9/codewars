package kyu6;

public class CountingDuplicates {
	public static int duplicateCount(String text) {
		char[] uniqueChars = new char[text.length()];
		int i = 0;
		for (int ch : text.toLowerCase().chars().distinct().toArray()) {
			uniqueChars[i] = (char)ch;
			++i;
		}
		int dupCount = 0;
		for (char c : uniqueChars) {
			if (text.toLowerCase().chars().filter(ch -> ch == c).count() > 1) {
				++dupCount;
			}
		}
		return dupCount;
	}
}
