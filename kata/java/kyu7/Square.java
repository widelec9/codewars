package kyu7;

public class Square {    
    public static boolean isSquare(int n) {
        Double nSqrt = Math.sqrt(n);
    	return n >= 0 && nSqrt == Math.round(nSqrt) && !Double.isInfinite(nSqrt);
    }
}