package kyu5;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class DirReduction {
	public static String[] dirReduc(String[] arr) {
		List<String> dir = new LinkedList<String>(Arrays.asList(arr));
		int i = dir.size();
		while (i > 0) {
			i -= 1;
			if ((i > 0) && ((dir.get(i - 1) == "NORTH" && dir.get(i) == "SOUTH")
					|| (dir.get(i - 1) == "SOUTH" && dir.get(i) == "NORTH")
					|| (dir.get(i - 1) == "EAST" && dir.get(i) == "WEST")
					|| (dir.get(i - 1) == "WEST" && dir.get(i) == "EAST"))) {
				dir.remove(i - 1);
				dir.remove(i - 1);
				i = dir.size();
			}
		}
		String[] retString = new String[dir.size()];
		dir.toArray(retString);
		return retString;
	}
}
