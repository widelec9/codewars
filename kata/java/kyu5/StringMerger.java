package kyu5;

import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;

public class StringMerger {
	public static boolean isMerge(String s, String part1, String part2) {
		char[] sChArr = s.toCharArray();
		List<Character> p1List = new LinkedList<Character>(part1.chars().mapToObj(c -> (char)c).collect(Collectors.toList()));
		List<Character> p2List = new LinkedList<Character>(part2.chars().mapToObj(c -> (char)c).collect(Collectors.toList()));
		boolean backCheck = false;
		
		int i = sChArr.length - 1;
		while (i >= 0) {
			if (p1List.size() > 0 && sChArr[i] == p1List.get(p1List.size() - 1)) {
				p1List.remove(p1List.size() - 1);
				i -= 1;
				backCheck = true;
			}
			else if (p2List.size() > 0 && sChArr[i] == p2List.get(p2List.size() - 1)) {
				p2List.remove(p2List.size() - 1);
				i -= 1;
				backCheck = false;
			}
			else if (backCheck == true && p2List.size() > 1 && sChArr[i] == p2List.get(p2List.size() - 2)) {
				p1List.add(p2List.remove(p2List.size() - 1));
				p2List.remove(p2List.size() - 1);
				i -= 1;
				backCheck = false;
			}
			else {
				return false;
			}
		}
		return (p1List.size() > 0 || p2List.size() > 0) ? false : true;
	}
}