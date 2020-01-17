package kyu5;

import java.util.Arrays;
import java.util.Comparator;

public class WeightSort {
	public static String orderWeight(String str) {
		String[] numStrings = str.split(" ");
		Arrays.sort(numStrings, new Comparator<String>() {
			@Override
			public int compare(String s1, String s2) {
				int n = s1.chars().map(ch -> ch - '0').sum() - s2.chars().map(ch -> ch - '0').sum();
				return n == 0 ? s1.compareTo(s2) : n;
			}
		});
		return String.join(" ", numStrings);
	}
}