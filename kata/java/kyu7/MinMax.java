package kyu7;

import java.util.Arrays;

class MinMax {
    public static int[] minMax(int[] arr) {
        int[] minmax = {Arrays.stream(arr).min().getAsInt(), Arrays.stream(arr).max().getAsInt()};
        return minmax;
    }
}
