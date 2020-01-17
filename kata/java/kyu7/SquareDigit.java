package kyu7;

public class SquareDigit {

	public int squareDigits(int n) {
		String nString = Integer.toString(n);
		StringBuilder sb = new StringBuilder("");
		for (int i = 0; i < nString.length(); ++i) {
			int digit = Integer.parseInt(String.valueOf(nString.charAt(i)));
			sb.append(digit * digit);
		}
		return Integer.parseInt(sb.toString());
	}

}