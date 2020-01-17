package kyu4;

import java.util.ArrayList;
import java.util.List;

public class Warrior {
	private int experience = 100;
	private String[] rankTable = {"Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"};
	private List<String> achievements = new ArrayList<>();

	private int addXp(int xpInc) {
		experience = Math.min(experience + xpInc, 10000);
		return experience;
	}
	
	public int experience() {
		return experience;
	}
	
	public int level() {
		return experience / 100;
	}
	
	public String rank() {
		return rankTable[experience / 1000];
	}
	
	public List<String> achievements() {
		return achievements;
	}
	
	public String training(String achv, int xp, int oppLvl) {
		String retString;
		if (level() >= oppLvl) {
			achievements.add(achv);
			addXp(xp);
			retString = achv;
		}
		else {
			retString = "Not strong enough";
		}
		return retString;
	}
	
	public String battle(int oppLvl) {
		String retString;
		if (!(1 <= oppLvl && oppLvl <= 100)) {
			retString = "Invalid level";
		}
		else {
			int diff = oppLvl - level();
			if (diff == -1) {
				addXp(5);
				retString = "A good fight";
			} else if (diff == 0) {
				addXp(10);
				retString = "A good fight";
			} else if (diff > 0) {
				if (diff >= 5 && oppLvl / 10 > level() / 10) {
					retString = "You've been defeated";
				}
				else {
					addXp(20 * (int)Math.pow(diff, 2));
					retString = "An intense fight";
				}
			} else {
				retString = "Easy fight";
			}
		}
		return retString;
	}
}
