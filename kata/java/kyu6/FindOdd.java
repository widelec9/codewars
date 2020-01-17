package kyu6;

import java.util.Arrays;

public class FindOdd {
	public static int findIt(int[] a) {
		int result = 0;
		for (int i : a) {
			if (Arrays.stream(a).filter(j -> j == i).count() % 2 == 1) {
				result = i;
				break;
			}
		}
		return result;
  }
}