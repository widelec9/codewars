package kyu6;

public class WhoLikesIt {
	public static String whoLikesIt(String... names) {
		String retString = "";
		switch (names.length) {
		case 0:	retString = "no one likes this"; break;
		case 1:	retString = String.format("%s likes this", names[0]); break;
		case 2:	retString = String.format("%s and %s like this", names[0], names[1]); break;
		case 3:	retString = String.format("%s, %s and %s like this", names[0], names[1], names[2]);	break;
		default: retString = String.format("%s, %s and %d others like this", names[0], names[1], names.length - 2);	break;
		}
		return retString;
	}
}
