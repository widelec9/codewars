package kyu6;

public class DRoot {
	public static int digital_root(int n) {
		int sum = 0;
		
		while (n / 10 > 0) {
			for (char c : String.valueOf(n).toCharArray()) {
				sum += c - '0';
			}
			n = sum;
			sum = 0;
		}
		return n;
	}
}