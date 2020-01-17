package kyu7;

import java.util.Arrays;
import java.util.Collections;

public class DescendingOrder {
	public static int sortDesc(final int num) {
		String[] numStrArr = String.valueOf(num).split("");
		Arrays.sort(numStrArr, Collections.reverseOrder());
		return Integer.parseInt(String.join("", numStrArr));
	}
}