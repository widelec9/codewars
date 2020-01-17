package kyu7;

import java.util.ArrayList;

class Metro {

	public static int countPassengers(ArrayList<int[]> stops) {
		int pax = 0;
		for (int[] stop : stops) {
			pax += stop[0] - stop[1];
		}
		return pax;
	}
}