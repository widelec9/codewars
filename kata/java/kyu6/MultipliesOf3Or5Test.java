package kyu6;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MultipliesOf3Or5Test {
	@Test
	public void test() {
		assertEquals(23, new MultipliesOf3Or5().solution(10));
	}

}