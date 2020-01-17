package kyu7;

public class JadenCase {

	public String toJadenCase(String phrase) {
		if (phrase != null && phrase.length() > 0) {
			String[] phraseSplit = phrase.split(" ");
			StringBuilder sb = new StringBuilder();
			for (String word : phraseSplit) {
				sb.append(Character.toUpperCase(word.charAt(0))).append(word.substring(1)).append(" ");
			}
			return sb.substring(0, sb.length() - 1).toString();
		}
		return null;
	}
}