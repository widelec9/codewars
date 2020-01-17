package kyu7;

public class Maskify {
    public static String maskify(String str) {
    	if (str.length() > 4) {
    		StringBuilder sb = new StringBuilder();
    		for (int i = 0; i < str.length()-4; ++i) {
    			sb.append('#');
    		}
    		str = sb.toString() + str.substring(str.length()-4);
    	}
    	return str;
    }
}
