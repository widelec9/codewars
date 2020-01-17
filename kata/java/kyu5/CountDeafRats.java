package kyu5;

public class CountDeafRats {
	private static int countDeafInRow(String ratsRow, byte piperDir) {
		int cnt = 0;
		String[] ratDir = {"~O", "O~"};
		
		for (int i = 0; i + 1 < ratsRow.length(); i += 2) {
			if (ratsRow.substring(i, i+2).equals(ratDir[piperDir])) {
				++cnt;
			}
		}
		return cnt;
	}
	
	public static int countDeafRats(final String town) {
		if (town.indexOf('O') == -1) {
			return 0;
		}
		
		String[] rats = town.replaceAll(" ", "").split("P");
		byte PIPER_LEFT = 0;
		byte PIPER_RIGHT = 1;
		int deaf = 0;

		if (rats.length == 1) {
			deaf = countDeafInRow(rats[0], PIPER_RIGHT);
		} else if (rats[0].equals("")) {
			deaf = countDeafInRow(rats[1], PIPER_LEFT);
		} else {
			deaf = countDeafInRow(rats[0], PIPER_RIGHT) + countDeafInRow(rats[1], PIPER_LEFT);
		}
		return deaf;
	}
}