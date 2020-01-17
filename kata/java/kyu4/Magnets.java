package kyu4;

//import java.util.stream.IntStream;

public class Magnets {
	public static double doubles(int maxk, int maxn) {
		double sum = 0;
		for (int n = 1; n < maxn + 1; ++n) {
			for (int k = 1; k < maxk + 1; ++k) {
				sum += Math.pow(n + 1, -2 * k) / k;
			}
		}
//		sum = IntStream.range(1, maxn+1).mapToDouble(n -> IntStream.range(1, maxk+1).mapToDouble(k -> Math.pow(n + 1, -2 * k) / k).sum()).sum();
		return sum;
	}
}
