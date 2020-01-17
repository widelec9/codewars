package kyu5;

public class LongToIP {
	public static String longToIP(long ip) {
		return String.format("%d.%d.%d.%d", ip >> 24, (ip >> 16) & 0xFF, (ip >> 8) & 0xFF, ip & 0xFF);
	}
}
