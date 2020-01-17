package kyu7;

import java.util.List;

public class BinaryArrayToNumber {
	public static int ConvertBinaryArrayToInt(List<Integer> binary) {
		StringBuilder sb = new StringBuilder();
		for (int i : binary) {
			sb.append(String.valueOf(i));
		}
		return Integer.parseInt(sb.toString(), 2);
	}
}