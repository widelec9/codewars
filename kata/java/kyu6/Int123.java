package kyu6;

public class Int123 {
	public static long int123(final int a) {
		long result = 0;
		
		if (a > 123) {
			result = Long.MAX_VALUE - (long) a + 123 + 1;
		}
		else if (a < 0) {
			result = Math.abs((long) a) + 123;
		}
		else {
			result = 123 - a;
		}

		return result;
	}
}