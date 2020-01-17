package kyu6;

import java.util.Arrays;

public class FindOutlier {
	static int find(int[] integers) {
		long oddCount = Arrays.stream(integers).filter(i -> Math.abs(i) % 2 == 1).count();
		if (oddCount == 1) {
			return Arrays.stream(integers).filter(i -> Math.abs(i) % 2 == 1).findFirst().getAsInt();
		}
		return Arrays.stream(integers).filter(i -> Math.abs(i) % 2 == 0).findFirst().getAsInt();
	}
}