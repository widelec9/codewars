package kyu5;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class LongToIPTest {
	@Test
	public void sampleTest() {
		assertEquals("128.114.17.104", LongToIP.longToIP(2154959208L));
		assertEquals("0.0.0.0", LongToIP.longToIP(0));
		assertEquals("128.32.10.1", LongToIP.longToIP(2149583361L));
	}
}
