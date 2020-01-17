package kyu5;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Tour {
	public static int tour(String[] arrFriends, String[][] ftwns, Map<String, Double> h) {
		List<String> listFriends = new ArrayList<String>(Arrays.asList(arrFriends));
		Map<String, String> ftwnsMap = new LinkedHashMap<String, String>();
		for (String[] ft : ftwns) {
			if (listFriends.contains(ft[0])) {
				ftwnsMap.put(ft[0], ft[1]);
			}
		}

		List<String> friendsTownGiven = new ArrayList<>(ftwnsMap.keySet());
		double dist = h.get(ftwnsMap.get(friendsTownGiven.get(0)));

		for (int i = 0; i < friendsTownGiven.size() - 1; ++i) {
			dist += Math.sqrt(Math.pow(h.get(ftwnsMap.get(friendsTownGiven.get(i + 1))), 2)
					- Math.pow(h.get(ftwnsMap.get(friendsTownGiven.get(i))), 2));
		}

		dist += h.get(ftwnsMap.get(friendsTownGiven.get(friendsTownGiven.size() - 1)));
		return (int) Math.floor(dist);
	}
}
