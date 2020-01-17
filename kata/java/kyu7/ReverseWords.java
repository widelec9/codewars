package kyu7;

public class ReverseWords {
	public static String reverseWords(final String original) {
		StringBuilder sb = new StringBuilder();
		StringBuilder subsb = new StringBuilder();
		if (original.chars().filter(c -> c == ' ').count() == original.length()) {
			return original;
		}
		for (String word : original.split(" ")) {
			sb.append(subsb.append(word).reverse().toString()).append(" ");
			subsb.setLength(0);
		}
		return sb.deleteCharAt(sb.length()-1).toString();
	}
}