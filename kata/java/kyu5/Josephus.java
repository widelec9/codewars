package kyu5;

import java.util.ArrayList;
import java.util.List;

public class Josephus {
	public static <T> List<T> josephusPermutation(final List<T> items, final int k) {
		List<T> result = new ArrayList<T>();
		List<T> itemsNew = new ArrayList<>(items);
		itemsNew.add(0, null);
		int i = 0;

		while (itemsNew.size() > 1) {
			int itemsNewSize = itemsNew.size();
			if (i == 0) {
				i += k;
			} else {
				if (itemsNewSize == 2) {
					i = 1;
				} else if (i + k > itemsNewSize) {
					i += k - itemsNewSize;
				} else {
					i += k - 1;
				}
			}

			while (i >= itemsNewSize) {
				i -= itemsNewSize - 1;
			}

			result.add(itemsNew.remove(i));
		}

		return result;
	}
}
