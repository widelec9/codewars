package kyu4;

import java.util.Arrays;
import java.util.stream.Collectors;

public class CarMileage {
	public static int isInteresting(int number, int[] awesomePhrases) {
		return isInteresting(number, awesomePhrases, 0);
	}
	
	private static int isInteresting(int number, int[] awesomePhrases, int depth) {
		int retVal = 0;
		String numString = String.valueOf(number);
		boolean followedByZeros = number > 99 ? numString.substring(1).matches("^[^1-9]+$") : false;
		boolean digIncDec = number > 99 ? "1234567890 9876543210".contains(numString) : false;
		boolean isPalindrome = number > 99 ? numString.equals(new StringBuilder(numString).reverse().toString()) : false;
		boolean isAwesome = number > 99 ? Arrays.stream(awesomePhrases).boxed().collect(Collectors.toList()).contains(number) : false;
		
		depth += 1;
		if (followedByZeros || digIncDec || isPalindrome || isAwesome) {
			retVal = 2;
		} else if (depth < 3 && (isInteresting(number+1, awesomePhrases, depth) == 2 || isInteresting(number+2, awesomePhrases, depth) == 2)) {
			retVal = 1;
		} else {
			retVal = 0;
		}
		return retVal;
	}
}
