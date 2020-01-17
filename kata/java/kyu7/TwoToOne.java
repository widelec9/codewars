package kyu7;

public class TwoToOne {

	public static String longest(String s1, String s2) {
		int[] chAscii = (s1+s2).toLowerCase().chars().distinct().sorted().toArray();
		StringBuilder sb = new StringBuilder();
		for (int i : chAscii) {
			sb.append((char)i);
		}
		return sb.toString();
	}
}