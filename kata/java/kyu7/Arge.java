package kyu7;

class Arge {

	public static int nbYear(int p0, double percent, int aug, int p) {
		int pCurrent = p0;
		int years = 0;
		while (pCurrent < p) {
			pCurrent += (pCurrent * percent / 100) + aug;
			++years;
		}
		return years;
	}
}