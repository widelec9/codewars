package kyu7;

class Kata {
	  public static String GetMiddle(String word) {
		  String retString;
		  int len = word.length();
		  if (len % 2 == 0) {
			  retString = word.substring(len / 2 - 1, (len / 2) + 1);
		  }
		  else {
			  retString = String.valueOf(word.charAt(len / 2));		  
		  }
		  return retString;
	  }
}