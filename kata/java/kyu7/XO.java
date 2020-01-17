package kyu7;

public class XO {

	public static boolean getXO(String str) {
		long xs = str.chars().filter(ch -> ch == 'x').count();
		long os = str.chars().filter(ch -> ch == 'o').count();
		return xs == os;
	}
}