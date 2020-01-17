package kyu8;

public class EvenOrOdd {
    public static String even_or_odd(int number) {
    	return Math.abs(number) % 2 == 1 ? "Odd" : "Even";
    }
}