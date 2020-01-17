package kyu7;

public class Printer {
	public static String printerError(String s) {
		long errorCount = s.chars().filter(ch -> ch > 'm').count();
		return String.format("%s/%s", String.valueOf(errorCount), String.valueOf(s.length()));
	}
}