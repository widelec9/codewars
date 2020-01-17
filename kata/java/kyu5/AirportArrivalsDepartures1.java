package kyu5;

import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

class AirportArrivalsDepartures1 {
	private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789";

	public static String[] flapDisplay(final String[] lines, final int[][] rotors) {
		String[] newLines = new String[lines.length];

		for (int l = 0; l < lines.length; ++l) {
			String line = lines[l];
			int[] rotor = rotors[l];
			StringBuilder newString = new StringBuilder();
			List<Character> tempLine = new LinkedList<>();

			for (int i = 0; i < rotor.length; ++i) {
				tempLine.clear();
				for (char c : line.toCharArray()) {
					tempLine.add(ALPHABET.charAt((ALPHABET.indexOf(c) + rotor[i]) % ALPHABET.length()));
				}
				line = tempLine.stream().map(String::valueOf).collect(Collectors.joining());
				newString.append(tempLine.get(i));
			}
			newLines[l] = newString.toString();
		}
		return newLines;
	}
}
