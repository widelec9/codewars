package kyu7;

public class ShortestWord {
	public static int findShort(String s) {
		int shortest = Integer.MAX_VALUE;
		for (String w : s.split(" ")) {
			if (w.length() < shortest) {
				shortest = w.length();
			}
		}

		return shortest;
	}
}