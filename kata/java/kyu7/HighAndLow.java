package kyu7;

import java.util.List;
import java.util.Arrays;
import static java.util.stream.Collectors.toList;

public class HighAndLow {
	public static String highAndLow(String numbers) {
		List<Integer> numList = Arrays.asList(numbers.split(" ")).stream().map(Integer::valueOf).collect(toList());
		numList.sort(null);
		return String.valueOf(numList.get(numList.size() - 1)) + " " + String.valueOf(numList.get(0));
	}
}
