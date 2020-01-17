package kyu6;

public class WhatTimeIsIt {
	public static String whatTimeIsIt(final double angle) {
		int MIN_PER_DEG = 2;
		int min = (int) Math.floor(angle * MIN_PER_DEG) % 720;
		int hour = min < 60 || min == 720 ? 12 : min / 60 % 60;
		return String.format("%02d:%02d", hour, min % 60);
	}
}