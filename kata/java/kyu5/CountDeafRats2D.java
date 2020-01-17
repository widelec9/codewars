package kyu5;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CountDeafRats2D {
	public static int countDeafRats(char[][] townSquare) {
		final Map<Character, byte[]> dirMap = new HashMap<Character, byte[]>();
		byte[] piperCoords = new byte[2];
		List<byte[]> ratCoords = new ArrayList<>();
		int deaf = 0;
		
		dirMap.put('↓', new byte[] { 1, 0 });
		dirMap.put('↑', new byte[] { -1, 0 });
		dirMap.put('→', new byte[] { 0, 1 });
		dirMap.put('←', new byte[] { 0, -1 });
		dirMap.put('↘', new byte[] { 1, 1 });
		dirMap.put('↖', new byte[] { -1, -1 });
		dirMap.put('↗', new byte[] { -1, 1 });
		dirMap.put('↙', new byte[] { 1, -1 });
		
		for (byte i = 0; i < townSquare.length; ++i) {
			for (byte j = 0; j < townSquare[i].length; ++j) {
				if (townSquare[i][j] != ' ') {
					if (townSquare[i][j] == 'P') {
						piperCoords[0] = i;
						piperCoords[1] = j;
					}
					else {
						ratCoords.add(new byte[] {i, j});
					}
				}
			}
		}
		
		for (byte[] rat : ratCoords) {
			char dir = townSquare[rat[0]][rat[1]];
			double distNow = Math.hypot(rat[0] - piperCoords[0], rat[1] - piperCoords[1]);
			double distNext = Math.hypot(rat[0] + dirMap.get(dir)[0] - piperCoords[0], rat[1] + dirMap.get(dir)[1] - piperCoords[1]);
			if (distNext > distNow) {
				++deaf;
			}
		}
		
		return deaf;
	}
}
