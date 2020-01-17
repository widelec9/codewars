package kyu5;

public class PigLatin {
	public static String pigIt(String str) {
		String[] words = str.split(" ");
		for (int i = 0; i < words.length; ++i) {
			if (words[i].matches("[A-Za-z]*")) {
				words[i] = words[i].substring(1) + words[i].charAt(0) + "ay";
			}
		}
		return String.join(" ", words);
	}
}