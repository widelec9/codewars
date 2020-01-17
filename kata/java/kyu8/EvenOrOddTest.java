package kyu8;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class EvenOrOddTest {
    @Test
    public void testEvenOrOdd() {
        assertEquals(EvenOrOdd.even_or_odd(6), "Even");
        assertEquals(EvenOrOdd.even_or_odd(7), "Odd");
        assertEquals(EvenOrOdd.even_or_odd(-1), "Odd");
    }
}
