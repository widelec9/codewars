package kyu6;

import java.util.stream.IntStream;

public class MultipliesOf3Or5 {
	public int solution(int number) {
		return IntStream.range(1, number).filter(i -> i % 3 == 0 || i % 5 == 0).sum();
	}
}
