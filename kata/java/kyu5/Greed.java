package kyu5;

import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Greed {
	public static int greedy(int[] dice) {
		int points = 0;

		Map<Integer, Long> diceCounterMap = IntStream.of(dice).mapToObj(d -> new Integer(d))
				.collect(Collectors.groupingBy(d -> d, Collectors.counting()));

		for (Map.Entry<Integer, Long> entry : diceCounterMap.entrySet()) {
			int k = entry.getKey();
			long v = entry.getValue();

			if (v >= 3) {
				switch (k) {
				case 1:
					points += 1000 + (v - 3) * 100;
					break;

				case 5:
					points += 500 + (v - 3) * 50;
					break;

				default:
					points += k * 100;
					break;
				}
			} else if (k == 1) {
				points += v * 100;
			} else if (k == 5) {
				points += v * 50;
			}
		}

		return points;
	}
}
