package kyu5;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Fracts {
	private static long gcd(long x, long y) {
		while (y > 0) {
			long temp = y;
			y = x % y;
			x = temp;
		}
		return x;
 	}
	
	private static long lcm(long x, long y) {
		return (x * y) / gcd(x, y);
	}
	
	public static String convertFrac(long[][] lst) {
		if (lst.length == 0) {
			return ""; 
		}
		
		List<long[]> simplifiedLst = Arrays.stream(lst).map(l -> new long[] {l[0] / gcd(l[0], l[1]), l[1] / gcd(l[0], l[1])}).collect(Collectors.toList());;
		List<Long> den = simplifiedLst.stream().map(l -> l[1]).collect(Collectors.toList());

		while (den.size() > 1) {
			den.set(0, lcm(den.get(0), den.remove(1)));
		}
		
		List<long[]> retList = simplifiedLst.stream().map(l -> new long[] {l[0] * (den.get(0) / l[1]), l[1] * (den.get(0) / l[1])}).collect(Collectors.toList());
		String[] retStrings = retList.stream().map(l -> String.format("(%d,%d)", l[0], l[1])).toArray(String[]::new);
		return String.join("", retStrings);
	}
}