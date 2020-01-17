package kyu7;

import java.util.HashMap;
import java.util.Map;

public class DnaStrand {
	public static String makeComplement(String dna) {
		Map<Character, Character> dict = new HashMap<Character, Character>();
		dict.put('A', 'T');
		dict.put('T', 'A');
		dict.put('G', 'C');
		dict.put('C', 'G');
		char[] chars = dna.toCharArray();

		for (int i = 0; i < dna.length(); ++i) {
			chars[i] = (dict.get(chars[i]));
		}

		return new String(chars);
	}
}